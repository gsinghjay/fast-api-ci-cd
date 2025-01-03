"""Service layer for user-related operations."""

import secrets
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from passlib.context import CryptContext

from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.utils.jwt import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    """Service class for handling user operations."""

    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        Hash a password for storing.

        Args:
            password: Plain text password

        Returns:
            str: Hashed password
        """
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify a password against a hash.

        Args:
            plain_password: Password to verify
            hashed_password: Hash to verify against

        Returns:
            bool: True if password matches hash
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        """
        Create a new user.

        Args:
            db: Database session
            user: User creation data

        Returns:
            User: Created user instance

        Raises:
            HTTPException: If user with email already exists
        """
        try:
            verification_token = secrets.token_urlsafe(32)
            db_user = User(
                email=user.email,
                full_name=user.full_name,
                hashed_password=UserService.get_password_hash(user.password),
                verification_token=verification_token,
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> User:
        """
        Authenticate a user.

        Args:
            db: Database session
            email: User email
            password: User password

        Returns:
            User: Authenticated user

        Raises:
            HTTPException: If authentication fails
        """
        user = db.query(User).filter(User.email == email).first()
        if not user or not UserService.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if not user.is_verified:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Please verify your email first",
            )
        return user

    @staticmethod
    def create_login_token(user: User) -> str:
        """
        Create a login token for a user.

        Args:
            user: User to create token for

        Returns:
            str: JWT access token
        """
        access_token = create_access_token(data={"sub": user.email, "role": user.role})
        return access_token

    @staticmethod
    def verify_email(db: Session, token: str) -> User:
        """
        Verify a user's email.

        Args:
            db: Database session
            token: Verification token

        Returns:
            User: Verified user

        Raises:
            HTTPException: If verification fails
        """
        user = db.query(User).filter(User.verification_token == token).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid verification token",
            )
        user.is_verified = True
        user.verification_token = None
        db.commit()
        return user

    @staticmethod
    def create_password_reset_token(db: Session, email: str) -> None:
        """
        Create a password reset token.

        Args:
            db: Database session
            email: User email

        Raises:
            HTTPException: If user not found
        """
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        user.password_reset_token = secrets.token_urlsafe(32)
        user.password_reset_expires = datetime.utcnow() + timedelta(hours=1)
        db.commit()

    @staticmethod
    def reset_password(db: Session, token: str, new_password: str) -> None:
        """
        Reset a user's password.

        Args:
            db: Database session
            token: Reset token
            new_password: New password

        Raises:
            HTTPException: If reset fails
        """
        user = (
            db.query(User)
            .filter(
                User.password_reset_token == token,
                User.password_reset_expires > datetime.utcnow(),
            )
            .first()
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired reset token",
            )
        user.hashed_password = UserService.get_password_hash(new_password)
        user.password_reset_token = None
        user.password_reset_expires = None
        db.commit()

"""Service layer for user-related operations."""

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from passlib.context import CryptContext

from app.models.user import User
from app.schemas.user_schema import UserCreate

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
            db_user = User(
                email=user.email,
                full_name=user.full_name,
                hashed_password=UserService.get_password_hash(user.password),
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400,
                detail="Email already registered",
            )

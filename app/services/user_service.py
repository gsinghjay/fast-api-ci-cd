"""User service module."""

from datetime import datetime, timedelta
from typing import Optional, Protocol

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import UserCreate


class UserServiceProtocol(Protocol):
    """Protocol defining the interface for UserService."""

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email.

        Args:
            email: User's email address

        Returns:
            Optional[User]: User object if found, None otherwise
        """
        ...

    def create(self, user: UserCreate) -> User:
        """Create a new user.

        Args:
            user: UserCreate schema containing user data

        Returns:
            User: Created user object
        """
        ...

    def verify_user(self, token: str) -> Optional[User]:
        """Verify user's email with token.

        Args:
            token: Verification token

        Returns:
            Optional[User]: Verified user object if successful, None otherwise
        """
        ...

    def authenticate(self, email: str, password: str) -> Optional[User]:
        """Authenticate user.

        Args:
            email: User's email address
            password: User's password

        Returns:
            Optional[User]: Authenticated user object if successful, None otherwise
        """
        ...

    def create_password_reset(self, email: str) -> bool:
        """Create password reset token.

        Args:
            email: User's email address

        Returns:
            bool: True if reset token was created, False otherwise
        """
        ...

    def reset_password(self, token: str, new_password: str) -> Optional[User]:
        """Reset user's password.

        Args:
            token: Password reset token
            new_password: New password to set

        Returns:
            Optional[User]: Updated user object if successful, None otherwise
        """
        ...


class UserService:
    """User service class for handling user-related operations."""

    def __init__(self) -> None:
        """Initialize UserService."""
        self.db: Session

    def __call__(self, db: Session) -> "UserService":
        """Make the service callable with a database session.

        Args:
            db: SQLAlchemy database session

        Returns:
            UserService: Service instance with database session
        """
        self.db = db
        return self

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email.

        Args:
            email: User's email address

        Returns:
            Optional[User]: User object if found, None otherwise
        """
        stmt = select(User).where(User.email == email)
        return self.db.execute(stmt).scalar_one_or_none()

    def create(self, user: UserCreate) -> User:
        """Create a new user.

        Args:
            user: UserCreate schema containing user data

        Returns:
            User: Created user object
        """
        db_user = User(
            email=user.email,
            full_name=user.full_name,
            password=get_password_hash(user.password),
            verification_token=self._generate_token(),
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def verify_user(self, token: str) -> Optional[User]:
        """Verify user's email with token.

        Args:
            token: Verification token

        Returns:
            Optional[User]: Verified user object if successful, None otherwise
        """
        user = self.db.query(User).filter(User.verification_token == token).first()
        if user:
            setattr(user, "is_verified", True)
            setattr(user, "verification_token", None)
            self.db.commit()
            self.db.refresh(user)
            return user
        return None

    def authenticate(self, email: str, password: str) -> Optional[User]:
        """Authenticate user.

        Args:
            email: User's email address
            password: User's password

        Returns:
            Optional[User]: Authenticated user object if successful, None otherwise
        """
        user = self.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def create_password_reset(self, email: str) -> bool:
        """Create password reset token.

        Args:
            email: User's email address

        Returns:
            bool: True if reset token was created, False otherwise
        """
        user = self.get_by_email(email)
        if not user:
            return False

        setattr(user, "password_reset_token", self._generate_token())
        setattr(user, "password_reset_expires", datetime.utcnow() + timedelta(hours=1))
        self.db.commit()
        return True

    def reset_password(self, token: str, new_password: str) -> Optional[User]:
        """Reset user's password.

        Args:
            token: Password reset token
            new_password: New password to set

        Returns:
            Optional[User]: Updated user object if successful, None otherwise
        """
        user = (
            self.db.query(User)
            .filter(
                User.password_reset_token == token,
                User.password_reset_expires > datetime.utcnow(),
            )
            .first()
        )
        if not user:
            return None

        setattr(user, "password", get_password_hash(new_password))
        setattr(user, "password_reset_token", None)
        setattr(user, "password_reset_expires", None)
        self.db.commit()
        self.db.refresh(user)
        return user

    def _generate_token(self) -> str:
        """Generate a random token.

        Returns:
            str: Generated token
        """
        import secrets

        return secrets.token_urlsafe(32)

"""User model definition."""

from datetime import datetime
import enum
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.models.base import Base


class UserRole(str, enum.Enum):
    """Enum for user roles."""

    USER = "user"
    ADMIN = "admin"


class User(Base):
    """
    User model for storing user information.

    Attributes:
        id (int): Primary key
        email (str): User's email address, unique
        full_name (str): User's full name
        password (str): Hashed password
        is_verified (bool): Email verification status
        role (str): User role (e.g., user, admin)
        verification_token (str): Token for email verification
        password_reset_token (str): Token for password reset
        password_reset_expires (datetime): Expiration time for password reset token
        last_login (datetime): Last login timestamp
        created_at (datetime): Account creation timestamp
        updated_at (datetime): Last update timestamp
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)
    role = Column(String, default=UserRole.USER)
    verification_token = Column(String, nullable=True)
    password_reset_token = Column(String, nullable=True)
    password_reset_expires = Column(DateTime, nullable=True)
    last_login = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

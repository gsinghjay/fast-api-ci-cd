"""Schema definitions for user-related operations."""

import re
from typing import Annotated, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr, field_validator, ConfigDict

from app.models.user import UserRole


class UserBase(BaseModel):
    """Base user schema with common attributes."""

    email: EmailStr
    full_name: Annotated[str, constr(min_length=1, max_length=100)]


class UserCreate(UserBase):
    """Schema for user registration request."""

    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        """
        Validate password strength.

        Args:
            v: Password to validate

        Returns:
            str: Validated password

        Raises:
            ValueError: If password doesn't meet requirements
        """
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character")
        return v


class UserLogin(BaseModel):
    """Schema for user login request."""

    email: EmailStr
    password: str


class Token(BaseModel):
    """Schema for token response."""

    access_token: str
    token_type: str = "bearer"


class UserResponse(UserBase):
    """Schema for user response."""

    id: int
    is_verified: bool
    role: UserRole
    last_login: Optional[datetime] = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class PasswordReset(BaseModel):
    """Schema for password reset request."""

    email: EmailStr


class PasswordResetConfirm(BaseModel):
    """Schema for password reset confirmation."""

    token: str
    new_password: str

    @field_validator("new_password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Validate password strength."""
        return UserCreate.validate_password(v)

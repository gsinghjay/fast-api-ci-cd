"""Router for user-related endpoints."""

from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    Token,
    PasswordReset,
    PasswordResetConfirm,
)
from app.services.user_service import UserService
from app.utils.db import get_db
from app.utils.dependencies import get_current_active_user
from app.models.user import User

router = APIRouter(prefix="/api/v1/users", tags=["users"])

# Create dependency instances
db_dependency = Depends(get_db)
oauth_form_dependency = Depends(OAuth2PasswordRequestForm)
current_user_dependency = Depends(get_current_active_user)


@router.post("/register", response_model=UserResponse, status_code=201)
def register_user(user: UserCreate, db: Session = db_dependency) -> UserResponse:
    """Register a new user.

    Args:
        user: User registration data
        db: Database session

    Returns:
        UserResponse: Created user data

    Raises:
        HTTPException: If registration fails
    """
    db_user = UserService.create_user(db, user)
    return UserResponse.model_validate(db_user)


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, oauth_form_dependency],
    db: Session = db_dependency,
) -> Token:
    """Authenticate user and create access token.

    Args:
        form_data: OAuth2 password request form
        db: Database session

    Returns:
        Token: JWT access token

    Raises:
        HTTPException: If authentication fails
    """
    user = UserService.authenticate_user(db, form_data.username, form_data.password)
    access_token = UserService.create_login_token(user)
    user.last_login = datetime.utcnow()
    db.commit()
    return Token(access_token=access_token)


@router.get("/me", response_model=UserResponse)
async def read_users_me(
    current_user: Annotated[User, current_user_dependency]
) -> UserResponse:
    """Get current user information.

    Args:
        current_user: Current authenticated user

    Returns:
        UserResponse: Current user data
    """
    return UserResponse.model_validate(current_user)


@router.get("/verify/{token}")
async def verify_email(token: str, db: Session = db_dependency) -> dict[str, str]:
    """Verify user email.

    Args:
        token: Verification token
        db: Database session

    Returns:
        dict: Success message

    Raises:
        HTTPException: If verification fails
    """
    UserService.verify_email(db, token)
    return {"message": "Email verified successfully"}


@router.post("/password-reset", status_code=status.HTTP_202_ACCEPTED)
async def request_password_reset(
    reset_request: PasswordReset, db: Session = db_dependency
) -> dict[str, str]:
    """Request password reset.

    Args:
        reset_request: Password reset request
        db: Database session

    Returns:
        dict: Success message
    """
    UserService.create_password_reset_token(db, reset_request.email)
    return {
        "message": "If your email is registered, you will receive a password reset link"
    }


@router.post("/password-reset/confirm")
async def confirm_password_reset(
    reset_confirm: PasswordResetConfirm, db: Session = db_dependency
) -> dict[str, str]:
    """Confirm password reset.

    Args:
        reset_confirm: Password reset confirmation
        db: Database session

    Returns:
        dict: Success message

    Raises:
        HTTPException: If reset fails
    """
    UserService.reset_password(db, reset_confirm.token, reset_confirm.new_password)
    return {"message": "Password reset successfully"}

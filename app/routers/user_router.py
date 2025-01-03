"""User router module."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, TokenResponse
from app.services.user_service import UserService, UserServiceProtocol
from app.core.database import get_db
from app.core.security import create_access_token

router = APIRouter(prefix="/api/v1/users", tags=["users"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def register_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    """
    Register a new user.

    Args:
        user: User registration data
        db: Database session

    Returns:
        User: Created user instance

    Raises:
        HTTPException: If user with email already exists
    """
    service: UserServiceProtocol = UserService()(db)
    existing_user = service.get_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return service.create(user)


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> dict[str, str]:
    """
    Authenticate user and create access token.

    Args:
        form_data: OAuth2 password request form
        db: Database session

    Returns:
        dict: Access token and token type

    Raises:
        HTTPException: If authentication fails
    """
    service: UserServiceProtocol = UserService()(db)
    user = service.authenticate(form_data.username, form_data.password)
    if not user:
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

    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/verify/{token}")
def verify_email(token: str, db: Session = Depends(get_db)) -> dict[str, str]:
    """
    Verify user's email with token.

    Args:
        token: Verification token
        db: Database session

    Returns:
        dict: Success message

    Raises:
        HTTPException: If verification fails
    """
    service: UserServiceProtocol = UserService()(db)
    user = service.verify_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid verification token",
        )
    return {"message": "Email verified successfully"}


@router.post("/password-reset", status_code=status.HTTP_202_ACCEPTED)
def request_password_reset(email: str, db: Session = Depends(get_db)) -> dict[str, str]:
    """
    Request password reset token.

    Args:
        email: User's email
        db: Database session

    Returns:
        dict: Success message
    """
    service: UserServiceProtocol = UserService()(db)
    if service.create_password_reset(email):
        return {"message": "If your email is registered, you will receive a reset link"}
    return {"message": "If your email is registered, you will receive a reset link"}


@router.post("/password-reset/confirm")
def reset_password(
    token: str, new_password: str, db: Session = Depends(get_db)
) -> dict[str, str]:
    """
    Reset user's password with token.

    Args:
        token: Reset token
        new_password: New password
        db: Database session

    Returns:
        dict: Success message

    Raises:
        HTTPException: If reset fails
    """
    service: UserServiceProtocol = UserService()(db)
    user = service.reset_password(token, new_password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired reset token",
        )
    return {"message": "Password reset successfully"}

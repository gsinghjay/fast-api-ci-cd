"""Authentication and authorization dependencies."""

from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.models.user import User, UserRole
from app.utils.db import get_db
from app.utils.jwt import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")

# Create dependency instances
db_dependency = Depends(get_db)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = db_dependency,
) -> User:
    """
    Get the current authenticated user.

    Args:
        token: JWT token
        db: Database session

    Returns:
        User: Current user

    Raises:
        HTTPException: If authentication fails
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = verify_token(token)
        email = str(payload.get("sub"))
        if not email:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    """
    Get the current active user.

    Args:
        current_user: Current authenticated user

    Returns:
        User: Current active user

    Raises:
        HTTPException: If user is not active
    """
    if not current_user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not verified",
        )
    return current_user


def check_admin_role(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    """
    Check if the current user has admin role.

    Args:
        current_user: Current active user

    Returns:
        User: Current admin user

    Raises:
        HTTPException: If user is not an admin
    """
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return current_user

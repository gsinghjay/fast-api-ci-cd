"""Router for user-related endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import UserService
from app.utils.db import get_db

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],
)

db_dependency = Depends(get_db)


@router.post("/register", response_model=UserResponse, status_code=201)
def register_user(
    user: UserCreate,
    db: Session = db_dependency,
) -> UserResponse:
    """
    Register a new user.

    Args:
        user: User registration data
        db: Database session

    Returns:
        UserResponse: Created user data

    Raises:
        HTTPException: If registration fails
    """
    return UserService.create_user(db, user)

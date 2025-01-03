"""Test authentication endpoints."""

from typing import Dict, Any, cast

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.services.user_service import UserService, UserServiceProtocol
from app.schemas.user import UserCreate


@pytest.fixture
def user_service() -> UserService:
    """Create a UserService instance.

    Returns:
        UserService: Service instance
    """
    return UserService()


@pytest.fixture
def test_user(db_session: Session, user_service: UserService) -> Dict[str, Any]:
    """Create a test user.

    Args:
        db_session: SQLAlchemy database session
        user_service: User service instance

    Returns:
        Dict[str, Any]: Test user data including ID
    """
    user_data: Dict[str, Any] = {
        "email": "test@example.com",
        "password": "Test123!@#",
        "full_name": "Test User",
    }
    service: UserServiceProtocol = user_service(db_session)
    user_create = UserCreate(**user_data)
    user = service.create(user_create)
    user_data["id"] = cast(int, user.id)
    return user_data


def test_login_success(test_client: TestClient, test_user: Dict[str, Any]) -> None:
    """Test successful login."""
    response = test_client.post(
        "/auth/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_unverified_user(
    test_client: TestClient, test_user: Dict[str, Any]
) -> None:
    """Test login with unverified user."""
    response = test_client.post(
        "/auth/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    assert response.status_code == 400
    assert "not verified" in response.json()["detail"].lower()


def test_password_reset_flow(
    test_client: TestClient, db_session: Session, user_service: UserService
) -> None:
    """Test password reset flow."""
    # Create a user
    user_data = {
        "email": "reset@example.com",
        "password": "OldPass123!@#",
        "full_name": "Reset User",
    }
    service: UserServiceProtocol = user_service(db_session)
    user_create = UserCreate(**user_data)
    user = service.create(user_create)

    # Request password reset
    response = test_client.post("/auth/password-reset", json={"email": user.email})
    assert response.status_code == 200

    # Get token from database
    token = cast(str, user.password_reset_token)
    assert token is not None

    # Reset password
    new_password = "NewPass123!@#"
    response = test_client.post(
        "/auth/password-reset/confirm",
        json={"token": token, "new_password": new_password},
    )
    assert response.status_code == 200

    # Try login with new password
    response = test_client.post(
        "/auth/login", data={"username": user.email, "password": new_password}
    )
    assert response.status_code == 200

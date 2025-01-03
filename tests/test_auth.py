"""Test cases for authentication endpoints."""

from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from app.models.base import Base


def test_login_success(test_client: TestClient, database_session: Session) -> None:
    """
    Test successful login.

    Should:
        - Allow registration
        - Verify email
        - Allow login
        - Return access token
    """
    # Register user
    user_data = {
        "email": "test@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Get verification token from database
    user = database_session.query(Base.metadata.tables["users"]).first()
    verification_token = user.verification_token

    # Verify email
    response = test_client.get(f"/api/v1/users/verify/{verification_token}")
    assert response.status_code == 200

    # Login
    response = test_client.post(
        "/api/v1/users/login",
        data={"username": user_data["email"], "password": user_data["password"]},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_unverified_user(test_client: TestClient) -> None:
    """
    Test login with unverified user.

    Should:
        - Allow registration
        - Deny login
    """
    # Register user
    user_data = {
        "email": "unverified@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Try to login
    response = test_client.post(
        "/api/v1/users/login",
        data={"username": user_data["email"], "password": user_data["password"]},
    )
    assert response.status_code == 401
    assert "verify" in response.json()["detail"].lower()


def test_password_reset_flow(
    test_client: TestClient, database_session: Session
) -> None:
    """
    Test password reset flow.

    Should:
        - Allow registration
        - Create reset token
        - Allow password reset
        - Allow login with new password
    """
    # Register user
    user_data = {
        "email": "reset@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Verify email
    user = database_session.query(Base.metadata.tables["users"]).first()
    verification_token = user.verification_token
    response = test_client.get(f"/api/v1/users/verify/{verification_token}")
    assert response.status_code == 200

    # Request password reset
    response = test_client.post(
        "/api/v1/users/password-reset",
        json={"email": user_data["email"]},
    )
    assert response.status_code == 202

    # Get reset token from database
    user = database_session.query(Base.metadata.tables["users"]).first()
    reset_token = user.password_reset_token

    # Reset password
    new_password = "NewStrongPass123!"
    response = test_client.post(
        "/api/v1/users/password-reset/confirm",
        json={"token": reset_token, "new_password": new_password},
    )
    assert response.status_code == 200

    # Login with new password
    response = test_client.post(
        "/api/v1/users/login",
        data={"username": user_data["email"], "password": new_password},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

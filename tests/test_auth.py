"""Test cases for authentication endpoints."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.models.base import Base
from app.utils.db import get_db
from app.models.user import UserRole

# Create in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True)
def setup_database():
    """Create tables before each test and drop them after."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    """Get test database session."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_login_success():
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
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Get verification token from database
    db = next(override_get_db())
    user = db.query(Base.metadata.tables["users"]).first()
    verification_token = user.verification_token

    # Verify email
    response = client.get(f"/api/v1/users/verify/{verification_token}")
    assert response.status_code == 200

    # Login
    response = client.post(
        "/api/v1/users/login",
        data={"username": user_data["email"], "password": user_data["password"]},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_unverified_user():
    """
    Test login with unverified user.

    Should:
        - Allow registration
        - Reject login for unverified user
    """
    user_data = {
        "email": "unverified@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Attempt login
    response = client.post(
        "/api/v1/users/login",
        data={"username": user_data["email"], "password": user_data["password"]},
    )
    assert response.status_code == 401
    assert "verify" in response.json()["detail"].lower()


def test_password_reset_flow():
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
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Request password reset
    response = client.post(
        "/api/v1/users/password-reset",
        json={"email": user_data["email"]},
    )
    assert response.status_code == 202

    # Get reset token from database
    db = next(override_get_db())
    user = db.query(Base.metadata.tables["users"]).first()
    reset_token = user.password_reset_token

    # Reset password
    new_password = "NewStrongPass123!"
    response = client.post(
        "/api/v1/users/password-reset/confirm",
        json={"token": reset_token, "new_password": new_password},
    )
    assert response.status_code == 200

    # Verify email for login
    response = client.get(f"/api/v1/users/verify/{user.verification_token}")
    assert response.status_code == 200

    # Try login with new password
    response = client.post(
        "/api/v1/users/login",
        data={"username": user_data["email"], "password": new_password},
    )
    assert response.status_code == 200


def test_get_current_user():
    """
    Test getting current user information.

    Should:
        - Allow registration
        - Verify email
        - Allow login
        - Return user information
    """
    # Register user
    user_data = {
        "email": "current@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Get verification token from database
    db = next(override_get_db())
    user = db.query(Base.metadata.tables["users"]).first()
    verification_token = user.verification_token

    # Verify email
    response = client.get(f"/api/v1/users/verify/{verification_token}")
    assert response.status_code == 200

    # Login
    response = client.post(
        "/api/v1/users/login",
        data={"username": user_data["email"], "password": user_data["password"]},
    )
    assert response.status_code == 200
    token = response.json()["access_token"]

    # Get current user
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
    assert response.json()["full_name"] == user_data["full_name"]
    assert response.json()["role"] == UserRole.USER

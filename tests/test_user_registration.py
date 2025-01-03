"""Test cases for user registration endpoints."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.models.base import Base
from app.utils.db import get_db

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


def test_register_user_success() -> None:
    """
    Test successful user registration.

    Should:
        - Return 201 status code
        - Return user data without password
        - Include user ID in response
    """
    user_data = {
        "email": "test@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["full_name"] == user_data["full_name"]
    assert "password" not in data
    assert "id" in data


def test_register_user_duplicate_email() -> None:
    """
    Test registration with duplicate email.

    Should:
        - Allow first registration
        - Reject second registration with same email
        - Return appropriate error message
    """
    user_data = {
        "email": "duplicate@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    # First registration
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Attempt duplicate registration
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 400
    assert "email already registered" in response.json()["detail"].lower()


def test_register_user_invalid_email() -> None:
    """
    Test registration with invalid email format.

    Should:
        - Return 422 status code
        - Reject invalid email format
    """
    user_data = {
        "email": "invalid-email",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 422


def test_register_user_weak_password() -> None:
    """
    Test registration with weak password.

    Should:
        - Return 422 status code
        - Reject password that doesn't meet strength requirements
    """
    user_data = {
        "email": "test@example.com",
        "password": "weak",
        "full_name": "Test User",
    }
    response = client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 422

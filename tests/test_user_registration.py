"""Test cases for user registration endpoints."""

from typing import Dict, Any

from fastapi.testclient import TestClient


def test_register_user_success(test_client: TestClient) -> None:
    """Test successful user registration.

    Args:
        test_client: FastAPI test client instance

    Tests:
        - Return 201 status code
        - Return user data without password
        - Include user ID in response
    """
    user_data: Dict[str, str] = {
        "email": "test@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201
    data: Dict[str, Any] = response.json()
    assert "id" in data
    assert data["email"] == user_data["email"]
    assert data["full_name"] == user_data["full_name"]
    assert "password" not in data


def test_register_user_duplicate_email(test_client: TestClient) -> None:
    """Test registration with duplicate email.

    Args:
        test_client: FastAPI test client instance

    Tests:
        - Allow first registration
        - Reject second registration with same email
        - Return appropriate error message
    """
    user_data: Dict[str, str] = {
        "email": "duplicate@example.com",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    # First registration
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Second registration with same email
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 400
    data: Dict[str, Any] = response.json()
    assert "detail" in data
    assert "already registered" in data["detail"].lower()


def test_register_user_invalid_email(test_client: TestClient) -> None:
    """Test registration with invalid email.

    Args:
        test_client: FastAPI test client instance

    Tests:
        - Return 422 status code
        - Return appropriate error message
    """
    user_data: Dict[str, str] = {
        "email": "invalid-email",
        "password": "StrongPass123!",
        "full_name": "Test User",
    }
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 422
    data: Dict[str, Any] = response.json()
    assert "detail" in data
    assert any("email" in error["loc"] for error in data["detail"])


def test_register_user_weak_password(test_client: TestClient) -> None:
    """Test registration with weak password.

    Args:
        test_client: FastAPI test client instance

    Tests:
        - Return 422 status code
        - Reject password that doesn't meet strength requirements
    """
    user_data: Dict[str, str] = {
        "email": "test@example.com",
        "password": "weak",
        "full_name": "Test User",
    }
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 422
    data: Dict[str, Any] = response.json()
    assert "detail" in data
    assert any("password" in error["loc"] for error in data["detail"])

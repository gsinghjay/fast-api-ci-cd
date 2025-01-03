"""Test cases for user registration endpoints."""

from fastapi.testclient import TestClient


def test_register_user_success(test_client: TestClient) -> None:
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
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["full_name"] == user_data["full_name"]
    assert "password" not in data
    assert "id" in data


def test_register_user_duplicate_email(test_client: TestClient) -> None:
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
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 201

    # Attempt duplicate registration
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 400
    assert "email already registered" in response.json()["detail"].lower()


def test_register_user_invalid_email(test_client: TestClient) -> None:
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
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 422


def test_register_user_weak_password(test_client: TestClient) -> None:
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
    response = test_client.post("/api/v1/users/register", json=user_data)
    assert response.status_code == 422

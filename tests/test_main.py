"""Tests for the main FastAPI application."""

from fastapi.testclient import TestClient
from app import __version__


def test_health_check(test_client: TestClient):
    """Test the health check endpoint."""
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "version": __version__}

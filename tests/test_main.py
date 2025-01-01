"""
Tests for the main FastAPI application.
"""
from fastapi.testclient import TestClient
from app.main import app
from app import __version__

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "version": __version__
    } 
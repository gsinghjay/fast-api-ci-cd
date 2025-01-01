"""
Tests for QR code generation functionality.
"""

from fastapi.testclient import TestClient
from app.main import app
import base64

client = TestClient(app)


def test_generate_qr_code():
    """Test QR code generation endpoint with default parameters."""
    response = client.post(
        "/qr/generate", json={"data": "https://example.com", "size": 10}
    )
    assert response.status_code == 200
    assert "qr_code" in response.json()

    # Verify the response contains a valid base64 encoded PNG
    qr_code = response.json()["qr_code"]
    try:
        decoded = base64.b64decode(qr_code)
        assert decoded.startswith(b"\x89PNG")  # PNG magic number
    except Exception:
        assert False, "Invalid base64 encoded PNG image"


def test_generate_qr_code_with_colors():
    """Test QR code generation endpoint with custom colors."""
    response = client.post(
        "/qr/generate",
        json={
            "data": "https://example.com",
            "size": 10,
            "fill_color": "#FF0000",  # Red
            "back_color": "#FFFFFF",  # White
        },
    )
    assert response.status_code == 200
    assert "qr_code" in response.json()

    # Verify the response contains a valid base64 encoded PNG
    qr_code = response.json()["qr_code"]
    try:
        decoded = base64.b64decode(qr_code)
        assert decoded.startswith(b"\x89PNG")  # PNG magic number
    except Exception:
        assert False, "Invalid base64 encoded PNG image"

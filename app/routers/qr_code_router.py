"""Router for QR code related endpoints."""

from fastapi import APIRouter
from app.schemas.qr_code_schemas import QRCodeRequest
from app.services.qr_code_service import generate_qr_code

router = APIRouter(prefix="/qr", tags=["QR Codes"])


@router.post("/generate")
async def create_qr_code(request: QRCodeRequest) -> dict[str, str]:
    """
    Generate a QR code from the provided data.

    Args:
        request: QR code generation request containing data, size, and colors

    Returns:
        dict: Contains the base64 encoded QR code image
    """
    qr_code = generate_qr_code(
        request.data, request.size, request.fill_color, request.back_color
    )
    return {"qr_code": qr_code}

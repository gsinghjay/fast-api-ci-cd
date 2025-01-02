"""QR Code generation endpoint module."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
import qrcode
from io import BytesIO
import base64

router = APIRouter()


class QRCodeRequest(BaseModel):
    """Request model for QR code generation."""

    url: HttpUrl
    fill_color: str = "#000000"  # Default to black
    background_color: str = "#FFFFFF"  # Default to white


@router.post("/generate")
async def generate_qr_code(request: QRCodeRequest):
    """
    Generate a QR code for the given URL with custom colors.

    Args:
        request (QRCodeRequest): Request containing URL and optional color
            settings.

    Returns:
        dict: A dictionary containing the base64 encoded QR code image.

    Raises:
        HTTPException: If there's an error generating the QR code.
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(str(request.url))
        qr.make(fit=True)

        # Create the QR code image with custom colors
        qr_image = qr.make_image(
            fill_color=request.fill_color, back_color=request.background_color
        )

        # Convert the image to base64
        buffered = BytesIO()
        qr_image.save(buffered)
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return {"qr_code": img_str}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

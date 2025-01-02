"""QR Code generation endpoint module."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl, Field, validator
import qrcode
from io import BytesIO
import base64
import re

router = APIRouter()


class QRCodeRequest(BaseModel):
    """Request model for QR code generation."""

    url: HttpUrl
    fill_color: str = "#000000"  # Default to black
    background_color: str = "#FFFFFF"  # Default to white
    box_size: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Size of each box in pixels",
    )
    border: int = Field(
        default=4,
        ge=0,
        le=20,
        description="Border size in boxes",
    )

    @validator("fill_color", "background_color")
    def validate_color(cls, v):
        """Validate color hex codes."""
        if not re.match(r"^#[0-9A-Fa-f]{6}$", v):
            raise ValueError("Color must be a valid hex code (e.g., #FF0000)")
        return v


@router.post("/generate")
async def generate_qr_code(request: QRCodeRequest):
    """
    Generate a QR code for the given URL with custom colors and size.

    Args:
        request (QRCodeRequest): Request containing URL and customization
            options:
            - url: The URL to encode
            - fill_color: Color of the QR code pattern (default: "#000000")
            - background_color: Color of the background (default: "#FFFFFF")
            - box_size: Size of each box in pixels (default: 10)
            - border: Border size in boxes (default: 4)

    Returns:
        dict: A dictionary containing the base64 encoded QR code image.

    Raises:
        HTTPException: If there's an error generating the QR code.
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=request.box_size,
            border=request.border,
        )
        qr.add_data(str(request.url))
        qr.make(fit=True)

        # Create the QR code image with custom colors
        qr_image = qr.make_image(
            fill_color=request.fill_color,
            back_color=request.background_color,
        )

        # Convert the image to base64
        buffered = BytesIO()
        qr_image.save(buffered)
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return {"qr_code": img_str}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

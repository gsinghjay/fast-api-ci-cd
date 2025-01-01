"""
Pydantic schemas for QR code related operations.
"""

from pydantic import BaseModel, Field


class QRCodeRequest(BaseModel):
    """Schema for QR code generation request."""

    data: str = Field(..., description="The data to encode in the QR code")
    size: int = Field(default=10, ge=1, le=40, description="QR code size (1-40)")
    fill_color: str = Field(
        default="black",
        description="QR code fill color (any valid color name or hex code)",
    )
    back_color: str = Field(
        default="white",
        description="QR code background color (any valid color name or hex code)",
    )

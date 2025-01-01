"""
Pydantic schemas for QR code related operations.
"""
from pydantic import BaseModel, Field

class QRCodeRequest(BaseModel):
    """Schema for QR code generation request."""
    data: str = Field(..., description="The data to encode in the QR code")
    size: int = Field(default=10, ge=1, le=40, description="QR code size (1-40)") 
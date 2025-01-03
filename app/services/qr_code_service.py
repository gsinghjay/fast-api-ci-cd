"""Service module for QR code generation."""

import qrcode
from io import BytesIO
import base64


def generate_qr_code(
    data: str, size: int = 10, fill_color: str = "black", back_color: str = "white"
) -> str:
    """
    Generate a QR code and return it as a base64 encoded string.

    Args:
        data: The data to encode in the QR code
        size: The size of the QR code (1-40)
        fill_color: Color of the QR code pattern (default: "black")
        back_color: Background color (default: "white")

    Returns:
        str: Base64 encoded PNG image
    """
    qr = qrcode.QRCode(
        version=1,  # Auto-size up to the specified size
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,  # Use size for box_size instead of version
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Convert PIL image to base64
    buffered = BytesIO()
    img.save(buffered)  # PNG is the default format
    return base64.b64encode(buffered.getvalue()).decode()

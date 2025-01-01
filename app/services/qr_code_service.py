"""
Service module for QR code generation.
"""
import qrcode
from io import BytesIO
import base64

def generate_qr_code(data: str, size: int = 10) -> str:
    """
    Generate a QR code and return it as a base64 encoded string.
    
    Args:
        data: The data to encode in the QR code
        size: The size of the QR code (1-40)
        
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

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert PIL image to base64
    buffered = BytesIO()
    img.save(buffered)  # PNG is the default format
    return base64.b64encode(buffered.getvalue()).decode() 
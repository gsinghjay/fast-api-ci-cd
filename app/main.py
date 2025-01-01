"""
Main FastAPI application module.
"""
from fastapi import FastAPI
from app import __version__

app = FastAPI(
    title="QR Code Generator",
    description="A robust and scalable QR Code Generator application",
    version=__version__
)

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the service is running.
    
    Returns:
        dict: Status information including version and status
    """
    return {
        "status": "healthy",
        "version": __version__
    } 
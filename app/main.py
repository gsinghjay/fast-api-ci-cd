"""Main FastAPI application module."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
import structlog
from app import __version__
from app.routers import qr_code_router
from app.utils.logging_config import configure_logging

# Configure logging
configure_logging()
logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events for the FastAPI application."""
    # Startup
    logger.info("application.startup", version=__version__)
    yield
    # Shutdown
    logger.info("application.shutdown")


app = FastAPI(
    title="QR Code Generator",
    description="A robust and scalable QR Code Generator application",
    version=__version__,
    lifespan=lifespan,
)

# Include routers
app.include_router(qr_code_router.router)


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the service is running.

    Returns:
        dict: Status information including version and status
    """
    logger.info("health_check.called")
    return {"status": "healthy", "version": __version__}

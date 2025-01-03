"""Main FastAPI application module."""

import os
from typing import Callable, Awaitable
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

from app import __version__
from app.routers.user_router import router as user_router
from app.routers.qr_code_router import router as qr_router
from app.middleware.rate_limiter import limiter, rate_limit_requests

app = FastAPI(title="QR Code Generator API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add rate limiter
app.state.limiter = limiter


async def rate_limit_handler(request: Request, exc: Exception) -> Response:
    """Handle rate limit exceeded exceptions.

    Args:
        request: The incoming request
        exc: The exception that was raised

    Returns:
        Response: JSON response with rate limit error details
    """
    if isinstance(exc, RateLimitExceeded):
        return JSONResponse(
            status_code=429,
            content={
                "detail": "Rate limit exceeded. Please try again later.",
                "type": "rate_limit_exceeded",
            },
            headers={"Retry-After": "60"},
        )
    raise exc


# Register the rate limit handler
app.add_exception_handler(RateLimitExceeded, rate_limit_handler)


@app.middleware("http")
async def rate_limit_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Apply rate limiting to all requests.

    Args:
        request: The incoming request
        call_next: The next middleware in the chain

    Returns:
        Response: The response from the next middleware
    """
    if os.getenv("TESTING") != "1":
        await rate_limit_requests(request)
    response = await call_next(request)
    return response


# Add routers
app.include_router(user_router)
app.include_router(qr_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        dict[str, str]: Health status and version information
    """
    return {"status": "healthy", "version": __version__}

"""Main FastAPI application module."""

import os
from typing import Any, Callable
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
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
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.middleware("http")
async def rate_limit_middleware(
    request: Request, call_next: Callable[[Request], Any]
) -> Response:
    """Apply rate limiting to all requests."""
    if os.getenv("TESTING") != "1":
        await rate_limit_requests(request)
    response = await call_next(request)
    return response


# Add routers
app.include_router(user_router)
app.include_router(qr_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "version": __version__}

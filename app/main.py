"""Main FastAPI application module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user_router, qr_code_router
from app.middleware.rate_limiter import RateLimiter

app = FastAPI(
    title="FastAPI CI/CD Example",
    description="A FastAPI example with CI/CD, authentication, and more",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add rate limiter middleware
app.add_middleware(RateLimiter)

# Include routers
app.include_router(user_router.router)
app.include_router(qr_code_router.router)


@app.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint.

    Returns:
        dict: Welcome message
    """
    return {"message": "Welcome to FastAPI CI/CD Example"}

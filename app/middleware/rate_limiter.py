"""Rate limiter middleware."""

import os
from fastapi import Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)


@limiter.limit("5/minute")
async def rate_limit_requests(request: Request):
    """Rate limit requests to 5 per minute per IP."""
    # Disable rate limiting during tests
    if os.getenv("TESTING") == "1":
        return

    # Check if rate limit is exceeded
    if await limiter.hit(request):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

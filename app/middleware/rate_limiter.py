"""Rate limiter middleware."""

import os
from typing import cast

from fastapi import Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address

# Initialize rate limiter with IP-based rate limiting
limiter: Limiter = Limiter(key_func=get_remote_address)


@limiter.limit("5/minute")
async def rate_limit_requests(request: Request) -> None:
    """Rate limit requests to 5 per minute per IP.

    Args:
        request: The incoming request to be rate limited

    Raises:
        HTTPException: When rate limit is exceeded (429 Too Many Requests)
            with Retry-After header set to 60 seconds

    Note:
        Rate limiting is disabled during testing (when TESTING=1)
        The type ignore for limiter.hit is required due to incomplete typings in slowapi
    """
    # Disable rate limiting during tests
    if os.getenv("TESTING") == "1":
        return

    # Check if rate limit is exceeded
    is_limited = cast(bool, await limiter.hit(request))  # type: ignore[attr-defined]
    if is_limited:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Please try again later.",
            headers={"Retry-After": "60"},
        )

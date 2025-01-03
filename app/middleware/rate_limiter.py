"""Rate limiter middleware for FastAPI."""

import time
from collections import defaultdict
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException, status


class RateLimiter(BaseHTTPMiddleware):
    """Rate limiter middleware."""

    def __init__(
        self,
        app,
        requests_per_minute: int = 60,
        auth_requests_per_minute: int = 5,
    ):
        """
        Initialize rate limiter.

        Args:
            app: FastAPI application
            requests_per_minute: Maximum requests per minute for general endpoints
            auth_requests_per_minute: Maximum requests per minute for auth endpoints
        """
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.auth_requests_per_minute = auth_requests_per_minute
        self.request_counts: defaultdict[str, list[float]] = defaultdict(list)

    async def dispatch(
        self,
        request: Request,
        call_next: Callable,
    ) -> Response:
        """
        Process each request through rate limiter.

        Args:
            request: FastAPI request
            call_next: Next middleware in chain

        Returns:
            Response: FastAPI response

        Raises:
            HTTPException: If rate limit exceeded
        """
        now = time.time()
        client_ip = request.client.host if request.client else "unknown"
        path = request.url.path

        # Determine rate limit based on endpoint
        is_auth_endpoint = path.startswith("/api/v1/users/")
        rate_limit = (
            self.auth_requests_per_minute
            if is_auth_endpoint
            else self.requests_per_minute
        )

        # Clean old requests
        self.request_counts[client_ip] = [
            req_time
            for req_time in self.request_counts[client_ip]
            if now - req_time < 60
        ]

        # Check rate limit
        if len(self.request_counts[client_ip]) >= rate_limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded",
            )

        # Add current request
        self.request_counts[client_ip].append(now)

        return await call_next(request)

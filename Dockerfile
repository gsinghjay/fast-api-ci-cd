# syntax=docker/dockerfile:1

FROM python:3.11-slim AS base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    wait-for-it \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry directly with version 1.8.5
RUN pip install poetry==1.8.5

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Configure Poetry
RUN poetry config virtualenvs.create false \
    && poetry config installer.max-workers 4

# Test stage
FROM base AS test

# Force poetry to update lock file and install dependencies
RUN poetry lock --no-update && \
    poetry install --no-interaction --no-ansi --with dev

# Copy test configurations
COPY pytest.ini .coveragerc ./
COPY tests/ ./tests/

# Copy application code
COPY app/ ./app/

# Set test environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV TESTING=1

# Update health check to verify database connection
HEALTHCHECK --interval=5s --timeout=5s --retries=3 \
    CMD pg_isready -h test-db -U postgres || exit 1

CMD ["tail", "-f", "/dev/null"]

# Production stage
FROM base AS production
RUN poetry install --no-interaction --no-ansi --without dev

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

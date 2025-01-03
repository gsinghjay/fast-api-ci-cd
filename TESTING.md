# Testing Guide

This guide covers all aspects of testing our FastAPI application using Docker Compose.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Detailed Testing Instructions](#detailed-testing-instructions)
- [Test Coverage](#test-coverage)
- [Debugging](#debugging)
- [Common Issues](#common-issues)
- [Best Practices](#best-practices)

## Prerequisites

- Docker and Docker Compose installed
- Poetry (optional, for local development)
- Git (for version control)

## Quick Start

1. **Run all tests at once:**
```bash
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit
```

2. **Run tests interactively:**
```bash
# Build fresh containers
docker compose -f docker-compose.test.yml build --no-cache

# Start services
docker compose -f docker-compose.test.yml up -d

# Run tests
docker compose -f docker-compose.test.yml exec test-app poetry run pytest -v
```

## Detailed Testing Instructions

### Setting Up Test Environment

1. **Create .env file:**
```bash
# Copy example env file
cp .env.example .env

# Edit as needed
nano .env
```

2. **Verify database connection:**
```bash
# Check database health
docker compose -f docker-compose.test.yml exec test-db pg_isready -U postgres
```

### Running Different Test Types

1. **Run all tests with coverage:**
```bash
docker compose -f docker-compose.test.yml exec test-app poetry run pytest -v --cov=app --cov-report=term-missing
```

2. **Run specific test files:**
```bash
# Run single test file
docker compose -f docker-compose.test.yml exec test-app poetry run pytest tests/test_specific.py -v

# Run specific test function
docker compose -f docker-compose.test.yml exec test-app poetry run pytest tests/test_specific.py::test_function -v

# Run tests matching pattern
docker compose -f docker-compose.test.yml exec test-app poetry run pytest -v -k "test_pattern"
```

3. **Run tests with different verbosity:**
```bash
# Normal verbosity
docker compose -f docker-compose.test.yml exec test-app poetry run pytest

# High verbosity
docker compose -f docker-compose.test.yml exec test-app poetry run pytest -vv

# Show locals in tracebacks
docker compose -f docker-compose.test.yml exec test-app poetry run pytest -l
```

## Test Coverage

1. **Generate coverage reports:**
```bash
# Terminal report
docker compose -f docker-compose.test.yml exec test-app poetry run pytest --cov=app --cov-report=term-missing

# HTML report
docker compose -f docker-compose.test.yml exec test-app poetry run pytest --cov=app --cov-report=html:/app/coverage/html

# XML report (for CI/CD)
docker compose -f docker-compose.test.yml exec test-app poetry run pytest --cov=app --cov-report=xml:/app/coverage/coverage.xml
```

2. **View coverage reports:**
- HTML reports are available in `./coverage/html/index.html`
- XML reports are in `./coverage/coverage.xml`

## Debugging

### Interactive Debugging

1. **Access container shell:**
```bash
docker compose -f docker-compose.test.yml exec test-app bash
```

2. **Run pytest with PDB:**
```bash
docker compose -f docker-compose.test.yml exec test-app poetry run pytest --pdb
```

3. **Debug specific test:**
```bash
docker compose -f docker-compose.test.yml exec test-app poetry run pytest -vv --pdb tests/test_specific.py::test_function
```

### Logging and Monitoring

1. **Watch logs in real-time:**
```bash
# All containers
docker compose -f docker-compose.test.yml logs -f

# Specific service
docker compose -f docker-compose.test.yml logs -f test-app
docker compose -f docker-compose.test.yml logs -f test-db
```

2. **Check container status:**
```bash
docker compose -f docker-compose.test.yml ps
```

## Common Issues

### Database Connection Issues

1. **Check database status:**
```bash
docker compose -f docker-compose.test.yml exec test-db pg_isready
```

2. **Verify environment variables:**
```bash
docker compose -f docker-compose.test.yml exec test-app env | grep POSTGRES
```

3. **Reset database:**
```bash
# Stop containers and remove volumes
docker compose -f docker-compose.test.yml down -v

# Restart fresh
docker compose -f docker-compose.test.yml up -d
```

### Container Issues

1. **Clean up containers:**
```bash
# Remove all test containers
docker compose -f docker-compose.test.yml down --remove-orphans

# Remove test volumes
docker volume rm fast-api-ci-cd_postgres_test_data
```

2. **Rebuild from scratch:**
```bash
# Full rebuild
docker compose -f docker-compose.test.yml build --no-cache
```

## Best Practices

1. **Always clean up after testing:**
```bash
docker compose -f docker-compose.test.yml down -v
```

2. **Use fresh builds for CI/CD:**
```bash
docker compose -f docker-compose.test.yml build --no-cache
```

3. **Regular maintenance:**
```bash
# Update dependencies
poetry update

# Regenerate lock file
poetry lock --no-update

# Rebuild containers
docker compose -f docker-compose.test.yml build --no-cache
```

## Environment Variables

Key environment variables for testing:
- `POSTGRES_USER`: Database user (default: postgres)
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Test database name (default: test_db)
- `POSTGRES_HOST`: Database host (default: test-db)
- `POSTGRES_PORT`: Database port (default: 5432)
- `TESTING`: Set to 1 for test mode
- `PYTHONPATH`: Set to /app
- `PYTHONUNBUFFERED`: Set to 1 for unbuffered output

## Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Poetry Documentation](https://python-poetry.org/docs/)

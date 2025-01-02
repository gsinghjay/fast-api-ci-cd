# FastAPI CI/CD Template

[![CI/CD Pipeline](https://github.com/gsinghjay/fast-api-ci-cd/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/gsinghjay/fast-api-ci-cd/actions/workflows/ci-cd.yml)
[![Latest Release](https://img.shields.io/github/v/release/gsinghjay/fast-api-ci-cd)](https://github.com/gsinghjay/fast-api-ci-cd/releases)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Code Coverage](https://img.shields.io/codecov/c/github/gsinghjay/fast-api-ci-cd)](https://codecov.io/gh/gsinghjay/fast-api-ci-cd)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready FastAPI template with robust CI/CD pipeline, semantic versioning, and best practices.

## 📑 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Development Guide](#️-development-guide)
- [Workflow Guide](#-workflow-guide)
- [Debugging Guide](#-debugging-guide)
- [Metrics and Monitoring](#-metrics-and-monitoring)
- [Environment Variables](#-environment-variables)
- [License](#-license)
- [Contributing](#-contributing)
- [Security](#-security)
- [Docker Support](#-docker-support)
- [API Documentation](#-api-documentation)
- [Performance](#-performance)
- [Testing](#-testing)
- [Error Handling](#-error-handling)

## 🌟 Features

- FastAPI-based RESTful API
- Poetry for dependency management
- Comprehensive CI/CD pipeline with GitHub Actions
- Semantic versioning and automated releases
- Automated changelog generation
- Code quality checks (Black, Commitlint)
- Test coverage reporting
- Prometheus metrics integration
- Structured logging with structlog
- Automated beta and release candidate versioning
- Branch-specific release configurations
- Detailed debugging and monitoring capabilities

## 📋 Prerequisites

- Python 3.9 or higher
- Poetry (Python package manager)
- Git
- Node.js 18+ (for commitlint)
- GitHub Personal Access Token (PAT) with repo scope

## 🚀 Quick Start

1. **Use this template**
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/fast-api-ci-cd
   cd fast-api-ci-cd
   ```

2. **Install dependencies**
   ```bash
   # Install Poetry
   curl -sSL https://install.python-poetry.org | python3 -

   # Install project dependencies
   poetry install

   # Install commitlint
   npm install -g @commitlint/cli @commitlint/config-conventional

   # Install semantic-release
   pip install python-semantic-release==9.15.0
   ```

3. **Set up pre-commit hooks**
   ```bash
   # Install pre-commit hooks
   poetry run pre-commit install
   poetry run pre-commit install --hook-type commit-msg
   ```

4. **Configure GitHub Token**
   ```bash
   # Add to your environment or .env file
   export GH_TOKEN=your_github_pat_token
   ```

5. **Run the application**
   ```bash
   # Development server with hot reload
   poetry run uvicorn app.main:app --reload --log-level debug

   # Production server
   poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

## 🔄 Workflow Guide

### Development Workflow

1. **Start a New Feature/Fix**
   ```bash
   # Create a new branch
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature  # or fix/your-fix
   ```

2. **Make Changes and Commit**
   ```bash
   # Stage changes
   git add .

   # Commit with conventional commit message
   git commit -m "feat(scope): add amazing feature"
   # or
   git commit -m "fix(scope): resolve specific issue"
   ```

3. **Push and Create PR**
   ```bash
   git push origin feature/your-feature
   # Create PR to develop branch via GitHub UI
   ```

4. **Release Process**
   ```bash
   # Beta releases (from develop)
   git checkout develop
   git pull origin develop
   # CI will automatically create beta release

   # Release candidates (from release/*)
   git checkout -b release/1.3.0
   git push origin release/1.3.0
   # CI will automatically create RC release

   # Final release (from main)
   # Create PR from develop to main
   # CI will create final release after merge
   ```

### Version Management

1. **Check Versions**
   ```bash
   # Current version
   poetry run semantic-release print-version --current

   # Next version
   poetry run semantic-release print-version --next
   ```

2. **Manual Release Trigger**
   ```bash
   # Via GitHub Actions UI:
   # - Set prerelease: true/false
   # - Set prerelease_token: beta/rc/alpha
   # - Set force: patch/minor/major
   # - Set build_metadata: (optional)
   ```

## 🐛 Debugging Guide

### Local Debugging

1. **Enable Debug Logging**
   ```bash
   # Run with debug logging
   poetry run uvicorn app.main:app --reload --log-level debug
   ```

2. **Use Debug Endpoints**
   ```bash
   # Health check
   curl http://localhost:8000/health

   # Debug info (development only)
   curl http://localhost:8000/debug/info
   ```

3. **Troubleshoot CI/CD**
   ```bash
   # Local semantic-release dry run
   poetry run semantic-release print-version --next

   # Verify git configuration
   git config --list

   # Check GitHub token
   gh auth status
   ```

### Common Issues

1. **Release Creation Fails**
   - Verify GitHub token permissions
   - Check branch protection rules
   - Ensure commit messages follow convention
   - Verify git user configuration

2. **Version Not Incrementing**
   - Check commit message format
   - Verify branch configuration in pyproject.toml
   - Check semantic-release logs in GitHub Actions

3. **Workflow Debugging**
   - Enable workflow debug logging:
     ```yaml
     env:
       ACTIONS_RUNNER_DEBUG: true
       ACTIONS_STEP_DEBUG: true
     ```

## 📊 Metrics and Monitoring

### Available Metrics

1. **Application Metrics** (at `/metrics`)
   - Request counts by endpoint
   - Response times (p50, p95, p99)
   - Error rates and types
   - Active connections
   - Resource utilization

2. **Custom Business Metrics**
   ```python
   # Example metric registration
   REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')

   # Example usage in endpoint
   @app.get("/")
   async def root():
       REQUEST_COUNT.inc()
       return {"message": "Hello World"}
   ```

### Monitoring Setup

1. **Prometheus Configuration**
   ```yaml
   scrape_configs:
     - job_name: 'fastapi'
       scrape_interval: 10s
       static_configs:
         - targets: ['localhost:8000']
   ```

2. **Grafana Dashboard**
   - Import provided dashboard template
   - Configure Prometheus data source
   - Set up alerting rules

### Health Checks

1. **Endpoints**
   ```bash
   # Basic health check
   curl http://localhost:8000/health

   # Detailed health status
   curl http://localhost:8000/health/detail

   # Readiness probe
   curl http://localhost:8000/ready
   ```

2. **Custom Health Checks**
   ```python
   # Example custom health check
   @app.get("/health/custom")
   async def custom_health():
       return {
           "status": "healthy",
           "checks": {
               "database": "connected",
               "cache": "available"
           }
       }
   ```

## 🔒 Environment Variables

Required environment variables:
- `GH_TOKEN`: GitHub token for releases (CI/CD)
- `LOG_LEVEL`: Logging level (debug/info/warning/error)
- `PORT`: Application port (default: 8000)
- `WORKERS`: Number of worker processes (default: 1)
- `METRICS_ENABLED`: Enable/disable Prometheus metrics (true/false)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit using conventional commits (`git commit -m "feat: add amazing feature"`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 🔐 Security

- All endpoints are rate-limited
- Input validation using Pydantic models
- CORS middleware configured
- Structured logging for audit trails
- Automated security scanning in CI/CD
- Signed commits required

## 🧪 Testing

```bash
# Run tests with coverage
poetry run pytest --cov=app tests/

# Generate coverage report
poetry run coverage html

# Run specific test file
poetry run pytest tests/test_specific.py -v

# Run tests with logging
poetry run pytest --log-cli-level=DEBUG
```

## 🚨 Error Handling

The API implements standardized error responses:
- 400: Bad Request - Invalid input
- 404: Not Found - Resource doesn't exist
- 429: Too Many Requests - Rate limit exceeded
- 500: Internal Server Error - Server-side issues

Custom error handling:
```python
@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "error_code": exc.error_code,
            "details": exc.details
        }
    )
```

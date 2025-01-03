# Contributing to FastAPI CI/CD Template

Thank you for your interest in contributing to our project! This document provides guidelines and workflows for contributing.

## 🔄 Development Workflow

### Prerequisites

1. Python 3.11
2. Poetry (for dependency management)
3. Node.js (for commit linting)
4. Git
5. PostgreSQL 14

### Initial Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/fast-api-ci-cd.git
   cd fast-api-ci-cd
   ```

2. **Install Dependencies**
   ```bash
   # Install Poetry
   curl -sSL https://install.python-poetry.org | python3 -

   # Install project dependencies
   poetry install

   # Install commit linting tools
   npm install

   # Install PostgreSQL (required for tests)
   # For Ubuntu/Debian:
   sudo apt-get update && sudo apt-get install -y postgresql-14 postgresql-server-dev-14
   # For macOS:
   brew install postgresql@14
   # For Windows:
   # Download and install from https://www.postgresql.org/download/windows/
   ```

3. **Set up Pre-commit Hooks**
   ```bash
   poetry run pre-commit install
   poetry run pre-commit install --hook-type commit-msg
   ```

### Code Quality Tools

We use several tools to maintain code quality:

1. **Black** - Code Formatting
   - Line length: 88 characters
   - Python target version: 3.11
   - Run with: `poetry run black .`

2. **Flake8** - Code Style and Quality Checks
   - Configuration in `.flake8`
   - Additional plugins:
     - `flake8-docstrings`: Docstring style checking
     - `flake8-bugbear`: Bug and design problem detection
     - `flake8-comprehensions`: List/dict/set comprehension checks
     - `flake8-simplify`: Code simplification suggestions
   - Run with: `poetry run flake8`

3. **MyPy** - Static Type Checking
   - Configuration in `pyproject.toml`
   - Strict type checking enabled
   - Type stub dependencies included
   - Pydantic plugin enabled
   - Run with: `poetry run mypy`

4. **Pre-commit** - Automated Quality Checks
   - Runs all linters before commit
   - Validates commit messages
   - Run manually: `poetry run pre-commit run --all-files`

### Development Process

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-fix-name
   ```

2. **Make Changes**
   - Write your code following our style guides:
     - Use type hints for function arguments and returns
     - Write docstrings for all public functions/classes
     - Keep docstrings concise and on one line when possible
     - Use descriptive variable names
   - Add tests
   - Update documentation
   - Run local checks:
     ```bash
     # Run all quality checks
     poetry run pre-commit run --all-files

     # Run tests
     poetry run pytest -v
     ```

3. **Commit Changes**
   We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

   ```bash
   # Format
   <type>(<scope>): <description>

   [optional body]

   [optional footer]
   ```

   Types:
   - `feat`: New feature (minor version)
   - `fix`: Bug fix (patch version)
   - `docs`: Documentation only
   - `style`: Code style changes
   - `refactor`: Code refactoring
   - `perf`: Performance improvements
   - `test`: Adding/updating tests
   - `chore`: Maintenance tasks

   Examples:
   ```bash
   feat(api): add new endpoint for user profiles
   fix(auth): resolve token expiration issue
   docs(readme): update installation instructions
   ```

4. **Push Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Go to GitHub and create a PR against the `main` branch
   - Fill out the PR template
   - Link related issues
   - Wait for CI checks to pass

## 🔍 CI/CD Pipeline

Our CI/CD pipeline automates testing, linting, and release processes. Here's what happens when you create a PR:

1. **Setup Environment**
   - Python 3.11 environment is created
   - Poetry and dependencies are installed
   - PostgreSQL service is started
   - Virtual environment is cached

2. **Quality Checks**
   - Black code formatting
   - Flake8 style checks
   - MyPy type checking
   - Pre-commit hooks validation

3. **Testing**
   - PostgreSQL database is initialized
   - Pytest runs all tests
   - Coverage report is generated
   - Test results are reported

4. **Release Process** (on main branch)
   - Semantic version is determined
   - Changelog is updated
   - Release is created
   - Assets are published

## 📝 Code Style Guidelines

1. **Python Code**
   - Follow PEP 8 guidelines
   - Use Black for formatting
   - Include type hints for all functions
   - Include docstrings for public functions/classes
   - Maximum line length: 88 characters (Black default)

2. **Commit Messages**
   - Follow Conventional Commits format
   - Keep first line under 72 characters
   - Use imperative mood ("add" not "added")
   - Reference issues when relevant

3. **Documentation**
   - Keep documentation up to date
   - Use clear, concise language
   - Include code examples when relevant
   - Update CHANGELOG.md for significant changes

## 🐛 Bug Reports

When filing a bug report, please include:

1. Python version
2. Operating system
3. PostgreSQL version
4. Steps to reproduce
5. Expected vs actual behavior
6. Relevant logs/screenshots
7. Possible fixes (if any)

## 🚀 Feature Requests

When proposing new features:

1. Explain the problem you're solving
2. Describe the proposed solution
3. Discuss alternatives considered
4. Consider backward compatibility
5. Include implementation details if possible

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [pytest-postgresql Documentation](https://pytest-postgresql.readthedocs.io/)

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the MIT License.

### Testing Process

1. **Unit Tests**
   - API endpoint tests
   - Database integration tests
   - PostgreSQL for test isolation
   ```bash
   poetry run pytest -v
   ```

2. **Test Coverage**
   - User registration tests:
     - Successful registration
     - Duplicate email handling
     - Password validation
     - Email format validation
   - QR code generation tests
   - Rate limiting tests
   - Health check endpoint tests

3. **Database Testing**
   - Tests use pytest-postgresql
   - Each test gets fresh database
   - Automatic cleanup after tests
   - Transaction rollback support

4. **API Testing**
   - FastAPI TestClient for endpoint testing
   - Request validation testing
   - Response schema validation
   - Error handling verification
   - Rate limit verification

### Database Workflow

1. **Development Database**
   ```bash
   # PostgreSQL connection settings
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=app
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   ```

2. **Test Database**
   ```bash
   # pytest-postgresql handles test database automatically
   # Configuration in pyproject.toml
   ```

3. **Database Migrations**
   - Models defined in `app/models/`
   - Tables created automatically on startup
   - Development uses PostgreSQL
   - Tests use pytest-postgresql

4. **Best Practices**
   - Use SQLAlchemy 2.0 style
   - Follow model-per-file pattern
   - Include proper indexes
   - Add type hints for models
   - Document model relationships

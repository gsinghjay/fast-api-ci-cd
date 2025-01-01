# FastAPI CI/CD Template

A production-ready FastAPI template with robust CI/CD pipeline, semantic versioning, and best practices.

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

## 📋 Prerequisites

- Python 3.9 or higher
- Poetry (Python package manager)
- Git
- Node.js 18+ (for commitlint)

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
   ```

3. **Set up pre-commit hooks**
   ```bash
   # Install pre-commit hooks
   poetry run pre-commit install
   poetry run pre-commit install --hook-type commit-msg
   ```

4. **Run the application**
   ```bash
   # Development server
   poetry run uvicorn app.main:app --reload

   # Production server
   poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## 🛠️ Development Guide

### Project Structure
```
fast-api-ci-cd/
├── .github/
│   └── workflows/           # CI/CD workflow definitions
├── app/
│   ├── __init__.py         # Version and app initialization
│   └── main.py             # Main FastAPI application
├── tests/                   # Test directory
├── .gitignore              # Git ignore rules
├── CHANGELOG.md            # Automated changelog
├── commitlint.config.js    # Commit message rules
├── poetry.lock            # Lock file for dependencies
├── pyproject.toml         # Project configuration
└── README.md              # This file
```

### Versioning System

This project uses semantic versioning (SemVer) with automated version management:

1. **Version Format**: `MAJOR.MINOR.PATCH` (e.g., 1.0.0)
2. **Version Bumps**:
   - `MAJOR`: Breaking changes (feat! or BREAKING CHANGE)
   - `MINOR`: New features (feat)
   - `PATCH`: Bug fixes (fix), performance improvements (perf), or refactoring (refactor)

### Commit Convention

We use Conventional Commits to automate versioning and changelog generation:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types**:
- `feat`: New feature (minor version bump)
- `fix`: Bug fix (patch version bump)
- `perf`: Performance improvement (patch version bump)
- `refactor`: Code refactoring (patch version bump)
- `docs`: Documentation changes
- `style`: Code style changes
- `test`: Adding/updating tests
- `chore`: Maintenance tasks

**Examples**:
```bash
# Feature (minor version bump)
git commit -m "feat(auth): add JWT authentication"

# Bug fix (patch version bump)
git commit -m "fix(api): handle null response in user service"

# Breaking change (major version bump)
git commit -m "feat(api)!: change authentication endpoint structure"
```

### CI/CD Pipeline

Our CI/CD pipeline consists of four main stages:

```mermaid
graph TD
    A[Push/PR] --> B{Lint}
    B -->|Success| C{Test}
    B -->|Failure| Z[Failed]
    C -->|Success| D{Branch = main?}
    C -->|Failure| Z
    D -->|Yes| E[Release]
    D -->|No| Y[End]
    E --> F[Tag Validation]
    F -->|Valid| G[Success]
    F -->|Invalid| H[Delete Tag]
```

1. **Lint Stage**:
   - Black code formatting
   - Commitlint message validation
   - Pre-commit hook checks

2. **Test Stage**:
   - Runs pytest with coverage
   - Generates coverage report
   - Updates changelog

3. **Release Stage** (main branch only):
   - Determines version bump from commits
   - Updates version files
   - Generates changelog
   - Creates GitHub release
   - Pushes git tag

4. **Tag Validation**:
   - Verifies tag authenticity
   - Ensures proper versioning

### Changelog Generation

The changelog is automatically generated and follows the Keep a Changelog format:

1. **Sections**:
   - Features
   - Bug Fixes
   - Breaking Changes
   - Documentation
   - Performance
   - Refactoring

2. **Generation Rules**:
   - Release commits are excluded
   - [skip ci] commits are excluded
   - Changelog updates are excluded

## 📊 Metrics and Monitoring

The application includes Prometheus metrics at `/metrics` endpoint for monitoring:
- Request counts
- Response times
- Error rates
- System metrics

## 🔒 Environment Variables

Required environment variables:
- `GH_TOKEN`: GitHub token for releases (CI/CD)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit using conventional commits (`git commit -m "feat: add amazing feature"`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

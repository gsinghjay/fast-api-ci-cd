# FastAPI CI/CD Template

[![CI/CD Pipeline](https://github.com/gsinghjay/fast-api-ci-cd/actions/workflows/ci.yml/badge.svg)](https://github.com/gsinghjay/fast-api-ci-cd/actions/workflows/ci.yml)
[![Latest Release](https://img.shields.io/github/v/release/gsinghjay/fast-api-ci-cd)](https://github.com/gsinghjay/fast-api-ci-cd/releases)
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready FastAPI template with robust CI/CD pipeline, semantic versioning, and best practices.

## 📑 Features

- FastAPI-based RESTful API with:
  - QR code generation
  - User registration with email validation
  - Secure password hashing using bcrypt
  - PostgreSQL database with pytest-postgresql for testing
  - Rate limiting with slowapi
- Poetry for dependency management
- Comprehensive CI/CD pipeline with GitHub Actions
  - Optimized caching strategy for dependencies
    - In-project Poetry virtual environments
    - Poetry package cache
    - Pip cache for Poetry installation
  - Matrix testing with Python 3.11
  - Automated dependency updates
  - PostgreSQL integration testing
- Robust code quality checks
  - Black for code formatting
  - Flake8 with advanced plugins:
    - flake8-docstrings for docstring validation
    - flake8-bugbear for bug detection
    - flake8-comprehensions for optimization
    - flake8-simplify for code simplification
  - MyPy for static type checking with strict type enforcement
  - Commitlint for commit message validation
  - Pre-commit hooks for automated validation
- Semantic versioning with automated releases
- Automated changelog generation on main branch
- Structured logging with structlog
- Prometheus metrics integration
- Conventional Commits standard
- Pull Request based workflow
- Release automation on main branch

## 🔄 Workflow Guide

### Development Workflow

1. **Create a Feature Branch**
   ```bash
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

3. **Create Pull Request**
   ```bash
   git push origin feature/your-feature
   # Create PR to main branch via GitHub UI
   ```

4. **Release Process**
   - Merging to main branch automatically:
     - Updates CHANGELOG.md
     - Creates a new release
     - Updates version numbers
     - Creates GitHub release with assets

### Commit Message Format

Follow the Angular Commit Message Convention:

```bash
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- feat: A new feature (MINOR version bump)
- fix: A bug fix (PATCH version bump)
- docs: Documentation only changes
- style: Changes that do not affect the meaning of the code
- refactor: A code change that neither fixes a bug nor adds a feature
- perf: A code change that improves performance
- test: Adding missing tests or correcting existing tests
- build: Changes that affect the build system or external dependencies
- ci: Changes to our CI configuration files and scripts
- chore: Other changes that don't modify src or test files

Breaking Changes:
- Add `BREAKING CHANGE:` in the footer
- Or append `!` after type/scope (e.g., `feat!:` or `feat(api)!:`)
- Triggers a MAJOR version bump

Examples:
```bash
# Feature with scope
feat(auth): add OAuth2 authentication

# Bug fix with breaking change
fix!: remove deprecated API endpoints

BREAKING CHANGE: The /v1/api/* endpoints have been removed.

# Documentation update
docs(readme): update installation instructions

# Multiple-line description with scope
feat(api): improve error handling for REST endpoints

Implement better error messages and status codes
for all REST API endpoints.

Closes #123
```

Scope:
- Optional parentheses-enclosed identifier
- Indicates section of codebase (e.g., api, auth, core)
- Should be noun describing the section

Description:
- Imperative, present tense: "change" not "changed" nor "changes"
- Don't capitalize first letter
- No period (.) at the end

Body:
- Free-form
- Provide context and motivation for changes
- Use imperative, present tense

Footer:
- Reference issues being closed
- Note breaking changes
- Multiple footers allowed
- Format: `token: value` or `BREAKING CHANGE: description`

## 🛠️ Development Setup

1. **Install Dependencies**
   ```bash
   # Install Poetry
   curl -sSL https://install.python-poetry.org | python3 -

   # Install project dependencies
   poetry install

   # Install commitlint
   npm install -g @commitlint/cli @commitlint/config-conventional

   # Install PostgreSQL (required for tests)
   # For Ubuntu/Debian:
   sudo apt-get update && sudo apt-get install -y postgresql-14 postgresql-server-dev-14
   # For macOS:
   brew install postgresql@14
   # For Windows:
   # Download and install from https://www.postgresql.org/download/windows/
   ```

2. **Set up Pre-commit Hooks**
   ```bash
   poetry run pre-commit install
   poetry run pre-commit install --hook-type commit-msg
   ```

3. **Configure GitHub Token**
   ```bash
   # Add to your environment
   export GH_TOKEN=your_github_pat_token
   ```

4. **Configure GitHub Actions**
   - Go to repository Settings → Secrets and variables → Actions
   - Add the following secrets:
     - `GH_TOKEN`: GitHub Personal Access Token with repo scope
     - `POSTGRES_USER`: PostgreSQL user for tests (default: postgres)
     - `POSTGRES_PASSWORD`: PostgreSQL password for tests
     - `POSTGRES_DB`: PostgreSQL database name for tests
   - Add the following variables:
     - `PYTHON_VERSION`: 3.11
     - `POETRY_VERSION`: Latest version (e.g., 1.7.1)

5. **Configure Branch Protection**
   - Go to Settings → Branches → Add rule
   - Branch name pattern: `main`
   - Enable:
     - Require pull request reviews
     - Dismiss stale pull request approvals
     - Require status checks to pass
     - Require branches to be up to date
     - Include administrators
   - Add required status checks:
     - `test`
     - `lint`
     - `type-check`

## 🚀 Running the Application

```bash
# Development server with hot reload
poetry run uvicorn app.main:app --reload --log-level debug

# Run tests
poetry run pytest -v

# Production server
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📝 API Documentation

### User Registration
```bash
curl -X POST "http://localhost:8000/api/v1/users/register" \
     -H "Content-Type: application/json" \
     -d '{
       "email": "user@example.com",
       "password": "StrongPass123!",
       "full_name": "John Doe"
     }'
```

Password requirements:
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character

Response (201 Created):
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe"
}
```

### Generate QR Code
```bash
curl -X POST "http://localhost:8000/api/v1/qr-code/generate" \
     -H "Content-Type: application/json" \
     -d '{
       "url": "https://example.com",
       "fill_color": "#000000",
       "background_color": "#FFFFFF",
       "box_size": 10,
       "border": 4
     }'
```

## 🔍 Environment Variables

Required environment variables:
- `GH_TOKEN`: GitHub token for releases
- `LOG_LEVEL`: Logging level (debug/info/warning/error)
- `PORT`: Application port (default: 8000)
- `WORKERS`: Number of worker processes (default: 1)
- `METRICS_ENABLED`: Enable/disable Prometheus metrics
- `POSTGRES_USER`: PostgreSQL user
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_DB`: PostgreSQL database name
- `POSTGRES_HOST`: PostgreSQL host (default: localhost)
- `POSTGRES_PORT`: PostgreSQL port (default: 5432)
- `RATE_LIMIT_PER_MINUTE`: Rate limit per minute per IP (default: 5)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Make changes following our commit conventions
4. Create a Pull Request to main branch
5. Ensure CI checks pass
6. Wait for review and merge

## 📚 Documentation

For more detailed documentation, see:
- [CHANGELOG.md](CHANGELOG.md) for version history
- [API Documentation](http://localhost:8000/docs) when running locally
- [GitHub Actions Workflows](.github/workflows) for CI/CD details

## 🔧 Setup Instructions

### Using This Template

1. **Create New Repository**
   - Click "Use this template" on GitHub
   - Or clone and reinitialize:
     ```bash
     git clone https://github.com/gsinghjay/fast-api-ci-cd
     cd fast-api-ci-cd
     rm -rf .git
     git init
     ```

2. **Configure GitHub Repository**
   - Go to repository Settings → Branches → Add rule
   - Protect `main` branch
   - Require pull request reviews
   - Require status checks to pass
   - Note: The workflows use `GITHUB_TOKEN` which is automatically provided by GitHub Actions

3. **Update Configuration Files**
   - Update `pyproject.toml`:
     ```toml
     [tool.poetry]
     name = "your-project-name"
     version = "1.0.0"
     authors = ["Your Name <your.email@example.com>"]
     ```
   - Update GitHub workflow files in `.github/workflows/`
   - Update repository URLs in documentation

### Workflow Debugging Commands

```bash
# List recent workflow runs
gh run list --limit 5

# Watch a specific workflow run
gh run watch

# View workflow run details
gh run view --log

# List failed workflow runs
gh run list --status failed

# Download workflow artifacts
gh run download <run-id>

# View workflow in browser
gh run view --web
```

### Common Issues & Solutions

1. **Release Creation Fails**
   - Check workflow permissions in repository settings
   - Ensure commit messages follow convention
   - Verify branch protection settings
   - Check git configuration:
     ```bash
     git config --list
     gh auth status
     ```

2. **Changelog Not Updating**
   - Only updates on main branch merges
   - Verify commit message format
   - Check workflow logs for errors
   - Ensure workflow has write permissions

3. **Pre-commit Hooks Failing**
   - Update hooks:
     ```bash
     pre-commit clean
     pre-commit autoupdate
     ```
   - Check commit message format
   - Run black manually:
     ```bash
     poetry run black .
     ```

4. **Workflow Permission Issues**
   - Repository Settings → Actions → General
   - Enable "Allow GitHub Actions to create and approve pull requests"
   - Check workflow permissions in yml files
   - Ensure proper permissions are set in workflow files

## 🔄 Semantic Versioning

This project follows [Semantic Versioning 2.0.0](https://semver.org/) principles. Version numbers are structured as MAJOR.MINOR.PATCH:

1. **MAJOR** version - Incremented for incompatible API changes
2. **MINOR** version - Incremented for backward-compatible new functionality
3. **PATCH** version - Incremented for backward-compatible bug fixes

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

### Version Bumping Rules

- Breaking changes (MAJOR): `BREAKING CHANGE:` in commit footer or `!` after type/scope
- New features (MINOR): `feat:` commit type
- Bug fixes (PATCH): `fix:` commit type
- No version bump: `chore:`, `docs:`, `style:`, `refactor:`, `perf:`, `test:`

## 🚀 Python Semantic Release

We use [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/) for automated versioning and changelog generation. Key features:

- Automatic version bumping based on commit messages
- Changelog generation following Keep a Changelog format
- GitHub release creation and asset publishing
- Support for pre-releases and build metadata

### Configuration

Configuration in `pyproject.toml` integrates our versioning and changelog standards:

```toml
[tool.python_semantic_release]
# Version Management
version_variables = ["app/__init__.py:__version__"]  # Update version in code
version_toml = ["pyproject.toml:tool.poetry.version"]  # Update version in pyproject.toml
version_source = ["tag", "commit"]  # Determine version from tags and commits
major_on_zero = false  # Follow SemVer for 0.x versions
tag_format = "v{version}"  # Git tag format (e.g., v1.0.0)

# Commit Parsing
commit_parser = "conventional_commits"  # Use Conventional Commits standard
commit_author = "github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>"

# Changelog Management
changelog_file = "CHANGELOG.md"  # Keep a Changelog file
changelog_sections = [  # Keep a Changelog categories
    "feature",    # Maps to Added
    "fix",        # Maps to Fixed
    "breaking",   # Maps to Changed with breaking changes
    "documentation",
    "performance",
    "refactor"
]

# Release Settings
upload_to_repository = false
build_command = "poetry build"
tag_type = "annotated"  # Use annotated tags for better documentation
```

### Automatic Standards Compliance

1. **Semantic Versioning**:
   - Analyzes commit messages using Conventional Commits
   - Automatically determines version bumps:
     - `BREAKING CHANGE` → MAJOR
     - `feat:` → MINOR
     - `fix:` → PATCH
   - Creates appropriate Git tags

2. **Keep a Changelog**:
   - Maintains CHANGELOG.md in the standard format
   - Groups changes by type (Added, Changed, Fixed, etc.)
   - Includes release dates and version links
   - Keeps an Unreleased section for upcoming changes
   - Links to Git comparisons between versions

### Manual Release Commands

```bash
# Check what the next version would be
poetry run semantic-release version --noop

# Create a new version (local only)
poetry run semantic-release version

# Create and publish a new release
poetry run semantic-release publish
```

### Environment Setup

Required environment variables:
- `GH_TOKEN`: GitHub Personal Access Token with `repo` scope
- For fine-grained tokens: `contents` permission required

## 🔄 Changelog Guidelines

We follow the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) principles for maintaining our CHANGELOG.md. This ensures our changelog is:

### Guiding Principles

- Written for humans, not machines
- Easy to link to any section
- One sub-section per version
- List releases in reverse-chronological order
- Include release date for each version
- Group changes by type
- Mention whether we follow Semantic Versioning

### Types of Changes

- `Added` - New features
- `Changed` - Changes in existing functionality
- `Deprecated` - Soon-to-be removed features
- `Removed` - Now removed features
- `Fixed` - Any bug fixes
- `Security` - In case of vulnerabilities

### Good Practices

- Keep an `Unreleased` section at the top for tracking upcoming changes
- Never use commit log diffs as changelog entries
- Always write clear, human-friendly descriptions
- Use ISO 8601 format for dates (YYYY-MM-DD)
- Make it clear when breaking changes occur
- Keep entries consistent and well-organized
- Link to issues, PRs, and other relevant information

### Example Entry

```markdown
## [1.0.0] - 2024-01-02

### Added
- New API endpoint for QR code generation
- Support for custom QR code colors

### Changed
- Improved error handling in API responses
- Updated dependencies to latest versions

### Fixed
- Issue with QR code size calculation
- Memory leak in image processing

[1.0.0]: https://github.com/username/project/compare/v0.9.0...v1.0.0
```

## 🔄 Workflow Architecture

```mermaid
flowchart TD
    subgraph "CI/CD Pipeline"
        A[Push/PR] --> B{Event Type?}

        B --> |PR/Push| C[Setup Python & PostgreSQL]
        C --> D[Install Dependencies]
        D --> E[Cache Environment]

        E --> F[Lint & Type Check]
        E --> G[Test with PostgreSQL]

        F & G --> H{All Checks Pass?}

        H -->|No| I[Report Failure]
        H -->|Yes & PR| J[Ready for Review]
        H -->|Yes & Push to Main| K[Semantic Release]

        K --> L[Generate Changelog]
        L --> M[Create Release]
        M --> N[Publish Assets]

        subgraph "Skip Release Conditions"
            S1[Skip if]
            S2[Commit by github-actions]
            S3["Message contains 'skip ci'"]
            S4["Message has 'chore(release)'"]
            S1 --> S2 & S3 & S4
        end
    end

    classDef trigger fill:#90EE90
    classDef setup fill:#FFE4B5
    classDef check fill:#FFB6C1
    classDef release fill:#ADD8E6
    classDef skip fill:#D3D3D3

    class A trigger
    class C,D,E setup
    class F,G,H check
    class K,L,M,N release
    class S1,S2,S3,S4 skip
```

### Workflow Files Structure

1. **CI Workflow** (.github/workflows/ci.yml)
   ```yaml
   name: CI
   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]

   jobs:
     test:
       runs-on: ubuntu-latest
       services:
         postgres:
           image: postgres:14
           env:
             POSTGRES_USER: ${{ secrets.POSTGRES_USER }}
             POSTGRES_PASSWORD: ${{ secrets.POSTGRES_PASSWORD }}
             POSTGRES_DB: ${{ secrets.POSTGRES_DB }}
           ports:
             - 5432:5432
           options: >-
             --health-cmd pg_isready
             --health-interval 10s
             --health-timeout 5s
             --health-retries 5
       steps:
         - uses: actions/checkout@v4
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: ${{ vars.PYTHON_VERSION }}
         - name: Install Poetry
           run: |
             curl -sSL https://install.python-poetry.org | python3 -
             poetry config virtualenvs.in-project true
         - name: Cache Poetry environment
           uses: actions/cache@v3
           with:
             path: .venv
             key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}
         - name: Install dependencies
           run: poetry install
         - name: Run tests
           run: poetry run pytest -v
           env:
             POSTGRES_USER: ${{ secrets.POSTGRES_USER }}
             POSTGRES_PASSWORD: ${{ secrets.POSTGRES_PASSWORD }}
             POSTGRES_DB: ${{ secrets.POSTGRES_DB }}
             POSTGRES_HOST: localhost
             POSTGRES_PORT: 5432

     lint:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: ${{ vars.PYTHON_VERSION }}
         - name: Install Poetry
           run: |
             curl -sSL https://install.python-poetry.org | python3 -
             poetry config virtualenvs.in-project true
         - name: Cache Poetry environment
           uses: actions/cache@v3
           with:
             path: .venv
             key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}
         - name: Install dependencies
           run: poetry install
         - name: Run linters
           run: |
             poetry run black . --check
             poetry run flake8
             poetry run mypy .
   ```

2. **Release Workflow** (.github/workflows/release.yml)
   ```yaml
   name: Release
   on:
     push:
       branches: [ main ]

   jobs:
     release:
       runs-on: ubuntu-latest
       if: "!contains(github.event.head_commit.message, 'chore(release)')"
       steps:
         - uses: actions/checkout@v4
           with:
             fetch-depth: 0
         - name: Python Semantic Release
           uses: python-semantic-release/python-semantic-release@v8.3.0
           with:
             github_token: ${{ secrets.GH_TOKEN }}
   ```

### Workflow Execution

1. **Setup Phase:**
   - Initializes Python 3.11 environment
   - Installs Poetry and dependencies
   - Creates virtual environment
   - Caches dependencies for speed
   - Shares environment via artifacts

2. **Parallel Checks:**
   - Lint and Test jobs run concurrently
   - Both use the shared virtual environment
   - All checks must pass to proceed

3. **Release Phase (Main Branch Only):**
   - Triggered on push to main
   - Uses python-semantic-release
   - Updates CHANGELOG.md
   - Creates GitHub release
   - Publishes release assets

### Skip Conditions

Workflow skips release when:
- Commit is from github-actions[bot]
- Commit message contains:
  - [skip ci]
  - chore(release)
- Event is a pull request

### Security and Permissions

- Uses built-in GITHUB_TOKEN
- Minimal required permissions per job:
  - Lint: read (contents, pull-requests)
  - Test: read (contents), write (checks)
  - Release: write (contents, id-token)

### Environment Optimization

- Shared virtual environment via artifacts
- Poetry for dependency management
- Cached dependencies:
  - Poetry virtual environment
  - Pip cache
  - Poetry package cache
- Preserved environment across jobs

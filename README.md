# FastAPI CI/CD Template

[![CI/CD Pipeline](https://github.com/gsinghjay/fast-api-ci-cd/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/gsinghjay/fast-api-ci-cd/actions/workflows/ci-cd.yml)
[![Latest Release](https://img.shields.io/github/v/release/gsinghjay/fast-api-ci-cd)](https://github.com/gsinghjay/fast-api-ci-cd/releases)
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready FastAPI template with robust CI/CD pipeline, semantic versioning, and best practices.

## 📑 Features

- FastAPI-based RESTful API with QR code generation
- Poetry for dependency management
- Comprehensive CI/CD pipeline with GitHub Actions
- Semantic versioning with automated releases
- Automated changelog generation on main branch
- Code quality checks (Black, Commitlint)
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

Follow the Conventional Commits standard:

```bash
type(scope): description

[optional body]

[optional footer]
```

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes
- refactor: Code refactoring
- perf: Performance improvements
- test: Adding/updating tests
- chore: Maintenance tasks

## 🛠️ Development Setup

1. **Install Dependencies**
   ```bash
   # Install Poetry
   curl -sSL https://install.python-poetry.org | python3 -

   # Install project dependencies
   poetry install

   # Install commitlint
   npm install -g @commitlint/cli @commitlint/config-conventional
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

## 🚀 Running the Application

```bash
# Development server
poetry run uvicorn app.main:app --reload --log-level debug

# Production server
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📝 API Documentation

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
   - Go to repository Settings → Secrets and Variables → Actions
   - Add `PAT_TOKEN` secret:
     - Generate token at GitHub → Settings → Developer settings → Personal access tokens
     - Required scopes: `repo`, `write:packages`
   - Configure branch protection rules:
     - Settings → Branches → Add rule
     - Protect `main` branch
     - Require pull request reviews
     - Require status checks to pass

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
   - Check PAT_TOKEN permissions
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
   - Ensure PAT_TOKEN has write permissions

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
   - Ensure PAT_TOKEN has required scopes
   - Check workflow permissions in yml files

## 🔄 Workflow Diagram

```mermaid
flowchart TD
    subgraph "CI/CD Pipeline"
        A[Push/PR] --> B{Event Type?}

        B -->|PR or Push| C[Lint Job]
        B -->|PR or Push| D[Test Job]

        C --> E{All Checks Pass?}
        D --> E

        E -->|Yes & Main Branch| F[Release Job]
        E -->|Yes & Feature Branch| G[Skip Release]

        F --> H[Semantic Release]
        H --> I{Released?}

        I -->|Yes| J[Publish Assets]
        I -->|No| K[Skip Publish]

        subgraph "Skip Conditions"
            P[Skip if:] --> P1[github-actions bot]
            P --> P2[skip ci tag]
            P --> P3[chore release]
        end
    end

    classDef trigger fill:#90EE90
    classDef check fill:#FFB6C1
    classDef release fill:#ADD8E6
    classDef publish fill:#98FB98

    class A trigger
    class E check
    class H release
    class J publish
```

### Workflow Steps Explained

1. **Trigger Events**
   - Pull Requests to any branch
   - Push to main branch
   - Manual workflow dispatch

2. **Lint Job**
   - Runs Black code formatter
   - Checks commit message format
   - Validates code style

3. **Test Job**
   - Runs pytest with coverage
   - Requires lint job success
   - Uses Python 3.11

4. **Release Job (main only)**
   - Creates semantic version
   - Updates CHANGELOG.md
   - Creates GitHub release
   - Publishes release assets

5. **Skip Conditions**
   - Bot commits
   - [skip ci] tags
   - Release commits

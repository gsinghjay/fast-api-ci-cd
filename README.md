README.md
# QR Code Generator Application

A robust and scalable QR Code Generator application built with FastAPI, featuring REPL integration, Prometheus and Grafana monitoring, structured logging, and secure user authentication. This application allows users to create, manage, and monitor QR codes efficiently.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [REPL Interface](#repl-interface)
- [Monitoring](#monitoring)
  - [Prometheus](#prometheus)
  - [Grafana](#grafana)
- [Logging](#logging)
- [Database Integration](#database-integration)
- [Dockerization](#dockerization)
- [Testing](#testing)
- [CI/CD Workflow for Python Backend](#cicd-workflow-for-python-backend)
  - [📄 Complete `ci-cd.yml` File with Integrated Tag Validation](#-complete-cicd.yml-file-with-integrated-tag-validation)
  - [📝 Detailed Breakdown and Comments](#-detailed-breakdown-and-comments)
- [Deployment](#deployment)
- [Continuous Integration/Continuous Deployment (CI/CD)](#continuous-integrationcontinuous-deployment-cicd)
- [Contributing](#contributing)
- [License](#license)

## Features

- **QR Code Generation:** Create customized QR codes with various options.
- **User Authentication:** Secure user signup and login with JWT-based authentication.
- **REPL Interface:** Interactive Read-Eval-Print Loop for developers to interact with the application components.
- **Monitoring:** Real-time monitoring using Prometheus and Grafana.
- **Structured Logging:** Enhanced logging for easier debugging and analysis.
- **Database Integration:** Persistent storage of QR codes and user data using PostgreSQL.
- **Docker Support:** Containerized application for easy deployment and scalability.
- **Continuous Integration/Continuous Deployment (CI/CD):** Automated testing and deployment pipelines.

## Technologies Used

- **Backend Framework:** FastAPI
- **Server:** Uvicorn
- **Database:** PostgreSQL with SQLAlchemy ORM
- **REPL:** ptpython
- **Monitoring:** Prometheus & Grafana
- **Logging:** Structlog
- **Containerization:** Docker & Docker Compose
- **Versioning & Dependency Management:** Poetry
- **Testing:** Pytest
- **CI/CD:** GitHub Actions
- **Others:** Alembic for migrations, Commitlint, Black for code formatting

## Project Structure

```
qr-code-generator/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── qr_code_router.py
│   │   └── user_router.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── qr_code_service.py
│   │   └── user_service.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── qr_code.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── qr_code_schemas.py
│   │   └── user_schemas.py
│   └── utils/
│       ├── __init__.py
│       ├── security.py
│       └── logging_config.py
├── tests/
│   ├── __init__.py
│   ├── test_qr_code.py
│   └── test_user.py
├── Dockerfile
├── docker-compose.yml
├── alembic/
│   └── ...
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.9+**
- **Docker & Docker Compose**
- **PostgreSQL**
- **pgAdmin (optional, for database management)**
- **Git**

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Set Up Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Using Poetry:

   ```bash
   poetry install
   ```

   Or using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Additional Tools**

   - **Commitlint**

     ```bash
     npm install --save-dev @commitlint/{config-conventional,cli}
     ```

   - **Black**

     ```bash
     pip install black
     ```

   - **Python Semantic Versioning**

     ```bash
     python3 -m pip install python-semantic-release
     ```

### Environment Setup

1. **Configure Environment Variables**

   Create a `.env` file in the project root and add the necessary environment variables:

   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/qr_code_db
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

2. **Database Migration**

   Apply database migrations using Alembic:

   ```bash
   alembic upgrade head
   ```

## Usage

### Running the Application

You can run the application locally using Uvicorn:

```bash
uvicorn app.main:app --reload
```

Or using Docker Compose:

```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:8000`.

### API Endpoints

#### Authentication

- **POST** `/users/signup` - Register a new user.
- **POST** `/users/login` - Authenticate a user and receive a JWT token.

#### QR Codes

- **POST** `/qr_codes` - Create a new QR code.
- **GET** `/qr_codes` - List all QR codes.
- **GET** `/qr_codes/{id}` - Retrieve a specific QR code by ID.
- **DELETE** `/qr_codes/{id}` - Delete a QR code.

#### Documentation

Interactive API documentation is available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## REPL Interface

An interactive REPL interface is available for developers to interact with the application components.

### Accessing the REPL

Activate the virtual environment and run:

```bash
ptpython
```

Within the REPL, you can import and interact with the application's services, models, and utilities for testing and development purposes.

## Monitoring

### Prometheus

Prometheus is used to collect metrics from the application.

- **Access Prometheus UI:** `http://localhost:9090`

### Grafana

Grafana is configured to visualize the metrics collected by Prometheus.

- **Access Grafana UI:** `http://localhost:3000`
- **Default Credentials:** `admin/admin`

#### Setting Up Dashboards

1. **Import Dashboards:** Use the provided dashboard configurations or create custom dashboards to monitor application performance metrics.
2. **Configure Data Sources:** Ensure Prometheus is added as a data source in Grafana.

## Logging

Structured logging is implemented using Structlog to provide context-rich log messages.

### Configuration

Logging configurations can be found in `app/utils/logging_config.py`. Logs include timestamps, request IDs, function names, and other relevant contextual information to facilitate easier debugging and analysis.

## Database Integration

The application uses PostgreSQL for persistent storage.

### Configuration

Database connection settings are managed via environment variables. SQLAlchemy is used as the ORM for interacting with the database.

### Managing Migrations

Alembic handles database migrations. To create a new migration after making model changes:

```bash
alembic revision --autogenerate -m "Your migration message"
alembic upgrade head
```

## Dockerization

Docker is used to containerize the application, ensuring consistency across different environments.

### Dockerfile

The `Dockerfile` defines the Docker image, specifying the base image, dependencies, and commands to run the application.

### Docker Compose

The `docker-compose.yml` file orchestrates multiple services:

- **FastAPI Application**
- **PostgreSQL Database**
- **Prometheus**
- **Grafana**
- **Nginx (optional, for serving static files)**

#### Running with Docker Compose

```bash
docker-compose up --build
```

## Testing

Comprehensive unit tests are implemented using Pytest to ensure the reliability of the application.

### Running Tests

```bash
pytest
```

### Test Coverage

Ensure that tests cover various aspects, including:

- API endpoints
- Service functions
- Data validation
- REPL interface

## CI/CD Workflow for Python Backend

### 📄 Complete `ci-cd.yml` File with Integrated Tag Validation

```yaml
# File: .github/workflows/ci-cd.yml

# Name of the workflow as it appears in the GitHub Actions tab
name: CI/CD Pipeline

# Define the events that trigger the workflow
on:
  # Trigger the workflow on push events to specific branches or tags
  push:
    branches:
      - "dev"      # Development branch
      - "main"     # Main/Production branch
    tags:
      - "v*"        # Tags following the pattern 'v*' (e.g., v1.0.0)
  # Trigger the workflow on pull request events targeting specific branches
  pull_request:
    branches:
      - "dev"
      - "main"

# Define permissions for the entire workflow
permissions:
  contents: write   # Grants write access to contents, necessary for deleting tags

# Control concurrency to ensure only the latest run for a branch/tag is active
concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: true  # Cancels any in-progress runs for the same ref

# Define all jobs within the workflow
jobs:
  ##########################################################################
  # 1. Lint Job
  ##########################################################################
  lint:
    name: Lint
    runs-on: ubuntu-latest  # Use the latest Ubuntu runner
    steps:
      - name: Check out code
        uses: actions/checkout@v3  # Checks out the repository code

      - name: Set up Node (for Commitlint)
        uses: actions/setup-node@v3
        with:
          node-version: 18  # Specify Node.js version

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"  # Specify Python version

      - name: Cache Poetry Dependencies
        uses: actions/cache@v3
        with:
          path: |
            ~/.cache/pypoetry  # Poetry cache directory
            ~/.cache/pip        # pip cache directory
          key: ${{ runner.os }}-poetry-${{ hashFiles('**/poetry.lock') }}  # Unique cache key based on OS and poetry.lock
          restore-keys: |
            ${{ runner.os }}-poetry-  # Fallback keys

      - name: Cache npm Dependencies
        uses: actions/cache@v3
        with:
          path: ~/.npm  # npm cache directory
          key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}  # Unique cache key based on OS and package-lock.json
          restore-keys: |
            ${{ runner.os }}-npm-  # Fallback keys

      - name: Install dependencies
        run: |
          # Install Python dependencies via Poetry without installing the root package
          pip install poetry
          poetry install --no-root

          # Install Node-based Commitlint globally
          npm install -g @commitlint/cli @commitlint/config-conventional

      - name: Lint code with Black
        run: black --check .  # Check Python code formatting with Black

      - name: Check commit messages with Commitlint
        run: |
          if [ "${{ github.event_name }}" = "pull_request" ]; then
            # Define the commit range for pull requests
            COMMIT_RANGE="${{ github.event.pull_request.base.sha }}..${{ github.event.pull_request.head.sha }}"
          else
            # Define the commit range for pushes (e.g., last 10 commits)
            COMMIT_RANGE="HEAD~10..HEAD"
          fi
          # Extract the first and last commit SHAs in the range
          COMMIT_FROM=$(git rev-parse $COMMIT_RANGE | head -n1)
          COMMIT_TO=$(git rev-parse $COMMIT_RANGE | tail -n1)
          # Run Commitlint on the specified commit range
          commitlint --from=$COMMIT_FROM --to=$COMMIT_TO

  ##########################################################################
  # 2. Test Job
  ##########################################################################
  test:
    name: Test
    runs-on: ubuntu-latest  # Use the latest Ubuntu runner
    needs: lint  # Ensure the 'lint' job completes before starting 'test'
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]  # Define Python versions for matrix testing
    steps:
      - name: Check out code
        uses: actions/checkout@v3  # Checks out the repository code

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}  # Use the Python version from the matrix

      - name: Cache Poetry Dependencies
        uses: actions/cache@v3
        with:
          path: |
            ~/.cache/pypoetry  # Poetry cache directory
            ~/.cache/pip        # pip cache directory
          key: ${{ runner.os }}-poetry-${{ hashFiles('**/poetry.lock') }}-py${{ matrix.python-version }}  # Unique cache key
          restore-keys: |
            ${{ runner.os }}-poetry-py${{ matrix.python-version }}-  # Fallback keys

      - name: Install dependencies
        run: |
          pip install poetry
          poetry install --no-root  # Install dependencies without the root package

      - name: Run tests with coverage
        run: |
          coverage run -m pytest  # Run tests with coverage
          coverage report -m      # Generate coverage report
          coverage xml            # Generate coverage XML for artifact

      - name: Upload coverage report
        uses: actions/upload-artifact@v3
        with:
          name: coverage-report-py${{ matrix.python-version }}  # Name of the artifact
          path: coverage.xml  # Path to the coverage report

  ##########################################################################
  # 3. Release Job (Runs only on tags that match v*)
  ##########################################################################
  release:
    name: Release
    if: startsWith(github.ref, 'refs/tags/v')  # Only run on tag pushes matching 'v*'
    needs: test  # Ensure the 'test' job completes before starting 'release'
    runs-on: ubuntu-latest  # Use the latest Ubuntu runner
    steps:
      - name: Check out code
        uses: actions/checkout@v3  # Checks out the repository code

      - name: Set up Node (for Commitlint)
        uses: actions/setup-node@v3
        with:
          node-version: 18  # Specify Node.js version

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"  # Specify Python version

      - name: Cache Poetry Dependencies
        uses: actions/cache@v3
        with:
          path: |
            ~/.cache/pypoetry  # Poetry cache directory
            ~/.cache/pip        # pip cache directory
          key: ${{ runner.os }}-poetry-${{ hashFiles('**/poetry.lock') }}  # Unique cache key
          restore-keys: |
            ${{ runner.os }}-poetry-  # Fallback keys

      - name: Cache npm Dependencies
        uses: actions/cache@v3
        with:
          path: ~/.npm  # npm cache directory
          key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}  # Unique cache key
          restore-keys: |
            ${{ runner.os }}-npm-  # Fallback keys

      - name: Install dependencies
        run: |
          pip install poetry
          poetry install --no-root  # Install Python dependencies without the root package
          pip install python-semantic-release  # Install Semantic Release for Python
          npm install -g @commitlint/cli @commitlint/config-conventional  # Install Commitlint globally

      - name: Verify Tag is on main Branch
        run: |
          # Fetch all branches to ensure origin/main is up to date
          git fetch origin main

          # Get the commit SHA that the tag points to
          TAG_COMMIT_SHA=$(git rev-parse $GITHUB_REF)

          # Get the latest commit SHA on main
          MAIN_COMMIT_SHA=$(git rev-parse origin/main)

          # Compare the tag commit SHA with the latest commit on main
          if [ "$TAG_COMMIT_SHA" != "$MAIN_COMMIT_SHA" ]; then
            echo "Error: Tag $GITHUB_REF is not pointing to the latest commit on main."
            exit 1  # Exit with error if the tag is not on the latest main commit
          fi

      - name: Run Semantic Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # GitHub token for release creation
        run: |
          semantic-release publish  # Execute Semantic Release to publish and tag

  ##########################################################################
  # 4. Tag Validation Job
  ##########################################################################
  tag-validation:
    name: Tag Validation
    if: startsWith(github.ref, 'refs/tags/v')  # Only run on tag pushes matching 'v*'
    needs: release  # Ensure the 'release' job completes before starting 'tag-validation'
    runs-on: ubuntu-latest  # Use the latest Ubuntu runner
    steps:
      - name: Check out code
        uses: actions/checkout@v3  # Checks out the repository code

      - name: Get Tag Details
        id: tag_details  # Assign an ID to reference outputs in subsequent steps
        run: |
          TAG_NAME=${GITHUB_REF#refs/tags/}  # Extract the tag name from the ref
          echo "tag_name=${TAG_NAME}" >> $GITHUB_OUTPUT  # Set the tag_name output

          # Get tagger information using git for-each-ref
          TAGGER_NAME=$(git for-each-ref refs/tags/$TAG_NAME --format='%(taggername)')
          TAGGER_EMAIL=$(git for-each-ref refs/tags/$TAG_NAME --format='%(taggeremail)')
          echo "tagger_name=${TAGGER_NAME}" >> $GITHUB_OUTPUT  # Set the tagger_name output
          echo "tagger_email=${TAGGER_EMAIL}" >> $GITHUB_OUTPUT  # Set the tagger_email output

      - name: Validate Tagger
        run: |
          # Define the expected tagger name/email (GitHub Actions bot)
          EXPECTED_TAGGER_NAME="github-actions[bot]"
          EXPECTED_TAGGER_EMAIL="41898282+github-actions[bot]@users.noreply.github.com"

          # Compare the actual tagger name and email with the expected values
          if [ "${{ steps.tag_details.outputs.tagger_name }}" != "$EXPECTED_TAGGER_NAME" ] || [ "${{ steps.tag_details.outputs.tagger_email }}" != "$EXPECTED_TAGGER_EMAIL" ]; then
            echo "Error: Tag ${{ steps.tag_details.outputs.tag_name }} was not created by GitHub Actions."
            # Delete the unauthorized tag using git push with :refs/tags/tag_name
            git push origin :refs/tags/${{ steps.tag_details.outputs.tag_name }}
            exit 1  # Exit with error if validation fails
          fi

      - name: Approve Tag
        run: echo "Tag ${{ steps.tag_details.outputs.tag_name }} is valid and created by GitHub Actions."  # Confirmation message

  ##########################################################################
  # 5. Update dev Branch to Next Dev Version
  ##########################################################################
  update-dev-version:
    name: Update dev Branch Version
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'  # Only run on pushes to main
    needs: release  # Ensure the 'release' job completes before starting 'update-dev-version'
    runs-on: ubuntu-latest  # Use the latest Ubuntu runner
    steps:
      - name: Check out dev branch
        uses: actions/checkout@v3
        with:
          ref: dev  # Ensure you're checking out the dev branch

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"  # Specify Python version

      - name: Cache Poetry Dependencies
        uses: actions/cache@v3
        with:
          path: |
            ~/.cache/pypoetry  # Poetry cache directory
            ~/.cache/pip        # pip cache directory
          key: ${{ runner.os }}-poetry-${{ hashFiles('**/poetry.lock') }}  # Unique cache key
          restore-keys: |
            ${{ runner.os }}-poetry-  # Fallback keys

      - name: Install dependencies
        run: |
          pip install poetry
          poetry install --no-root  # Install dependencies without the root package
          pip install python-semantic-release  # Install Semantic Release for Python

      - name: Update Version to Next Dev Version
        run: |
          # Configure Semantic Release for dev branch to bump to the next dev version
          semantic-release version --version-dev

      - name: Commit and Push Changes
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # GitHub token for pushing changes
        run: |
          # Configure Git user for committing
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add your_package/__init__.py  # Update the path accordingly to your version file
          git commit -m "chore(release): bump version to next dev version [skip ci]"  # Commit message with [skip ci] to prevent triggering workflows
          git push origin dev  # Push changes to the dev branch

  ##########################################################################
  # 6. Post-Merge Verification Job
  ##########################################################################
  post-merge-verification:
    name: Post-Merge Verification
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'  # Only run on pushes to main
    needs: [lint, test, release, update-dev-version]  # Ensure all prior jobs complete successfully
    runs-on: ubuntu-latest  # Use the latest Ubuntu runner
    steps:
      - name: Check out code
        uses: actions/checkout@v3  # Checks out the repository code

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"  # Specify Python version

      - name: Cache Poetry Dependencies
        uses: actions/cache@v3
        with:
          path: |
            ~/.cache/pypoetry  # Poetry cache directory
            ~/.cache/pip        # pip cache directory
          key: ${{ runner.os }}-poetry-${{ hashFiles('**/poetry.lock') }}  # Unique cache key
          restore-keys: |
            ${{ runner.os }}-poetry-  # Fallback keys

      - name: Install dependencies
        run: |
          pip install poetry
          poetry install --no-root  # Install dependencies without the root package

      - name: Run critical post-merge checks
        run: |
          # Re-run essential tests to ensure stability after merging
          coverage run -m pytest
          coverage report -m
          # Optionally, add deployment steps here (e.g., deploy to production)

      - name: Notify Deployment Success
        uses: some-notification-action@v1  # Replace with your preferred notification action
        with:
          message: "🚀 Deployment to Production Successful! 🎉"  # Custom notification message
```

### 📝 Detailed Breakdown and Comments

#### 1. **Workflow Triggers (`on` Section)**

- **Push Events:**
  - **Branches:** The workflow triggers on pushes to both `dev` and `main` branches.
  - **Tags:** It also triggers on any tag that matches the pattern `v*`, such as `v1.0.0`.
- **Pull Request Events:**
  - The workflow runs on pull requests targeting the `dev` and `main` branches.

#### 2. **Permissions**

- **`contents: write`:**
  - Grants the workflow write permissions to the repository contents.
  - **Purpose:** Necessary for the **Tag Validation** job to delete unauthorized tags if validation fails.

#### 3. **Concurrency Control**

- **`group: ${{ github.ref }}`:**
  - Groups concurrent runs by the Git reference (branch or tag).
- **`cancel-in-progress: true`:**
  - Ensures that if a new commit is pushed to the same branch or tag while a workflow run is in progress, the previous run is canceled in favor of the new one. This optimizes resource usage and ensures the pipeline reflects the latest code state.

#### 4. **Jobs Overview**

The workflow consists of six main jobs:

1. **Lint**
2. **Test**
3. **Release**
4. **Tag Validation**
5. **Update dev Branch Version**
6. **Post-Merge Verification**

Each job is defined with specific triggers, dependencies (`needs`), and steps to perform its tasks.

---

### 4. **Job: Lint**

- **Purpose:**
  - Ensures code quality by checking Python code formatting and validating commit messages.
- **Steps:**
  - **Check out code:** Retrieves the repository code.
  - **Set up Node & Python:** Prepares the necessary environments.
  - **Cache Dependencies:** Caches Poetry and npm dependencies to speed up subsequent runs.
  - **Install Dependencies:** Installs Python dependencies via Poetry and Commitlint for commit message validation.
  - **Lint with Black:** Checks Python code formatting.
  - **Check Commit Messages:** Validates commit messages against Conventional Commits standards using Commitlint.

---

### 5. **Job: Test**

- **Purpose:**
  - Runs automated tests across multiple Python versions to ensure compatibility and reliability.
- **Dependencies:**
  - **`needs: lint`:** Ensures that linting passes before testing begins.
- **Strategy:**
  - **Matrix Testing:** Executes the test suite on Python versions 3.8, 3.9, and 3.10 concurrently.
- **Steps:**
  - **Check out code:** Retrieves the repository code.
  - **Set up Python:** Prepares the Python environment based on the matrix.
  - **Cache Dependencies:** Caches Poetry dependencies specific to each Python version.
  - **Install Dependencies:** Installs Python dependencies via Poetry.
  - **Run Tests with Coverage:** Executes tests using Pytest and generates coverage reports.
  - **Upload Coverage Report:** Saves the coverage report as an artifact for later reference.

---

### 6. **Job: Release**

- **Purpose:**
  - Automates the release process by publishing new versions and tagging commits.
- **Trigger:**
  - **`if: startsWith(github.ref, 'refs/tags/v')`:** Only runs when a tag matching `v*` is pushed.
- **Dependencies:**
  - **`needs: test`:** Ensures that all tests pass before attempting a release.
- **Steps:**
  - **Check out code:** Retrieves the repository code.
  - **Set up Node & Python:** Prepares the necessary environments.
  - **Cache Dependencies:** Caches Poetry and npm dependencies.
  - **Install Dependencies:** Installs Python dependencies, Semantic Release, and Commitlint.
  - **Verify Tag is on main Branch:** Confirms that the tag points to the latest commit on `main` to prevent releasing from outdated commits.
  - **Run Semantic Release:** Executes Semantic Release to publish the new version and create the corresponding tag.

---

### 7. **Job: Tag Validation**

- **Purpose:**
  - Ensures that tags are created exclusively by the GitHub Actions bot, maintaining the integrity of release tags.
- **Trigger:**
  - **`if: startsWith(github.ref, 'refs/tags/v')`:** Only runs when a tag matching `v*` is pushed.
- **Dependencies:**
  - **`needs: release`:** Ensures that the release job completes successfully before validating the tag.
- **Steps:**
  - **Check out code:** Retrieves the repository code.
  - **Get Tag Details:** Extracts the tag name, tagger's name, and email from the pushed tag.
  - **Validate Tagger:**
    - Compares the actual tagger's name and email with the expected values (`github-actions[bot]`).
    - If the tag was not created by the GitHub Actions bot, it deletes the unauthorized tag and fails the job.
  - **Approve Tag:** Confirms that the tag is valid and was created by the GitHub Actions bot.

---

### 8. **Job: Update dev Branch Version**

- **Purpose:**
  - Automatically updates the `dev` branch to the next development version after a successful release.
- **Trigger:**
  - **`if: github.ref == 'refs/heads/main' && github.event_name == 'push'`:** Only runs on pushes to the `main` branch.
- **Dependencies:**
  - **`needs: release`:** Ensures that the release job completes successfully before updating the `dev` branch.
- **Steps:**
  - **Check out dev branch:** Retrieves the `dev` branch code.
  - **Set up Python:** Prepares the Python environment.
  - **Cache Dependencies:** Caches Poetry dependencies.
  - **Install Dependencies:** Installs Python dependencies and Semantic Release.
  - **Update Version to Next Dev Version:** Uses Semantic Release to bump the version to the next development version (e.g., from `v1.0.0` to `v1.1.0-dev`).
  - **Commit and Push Changes:** Commits the version bump and pushes the changes to the `dev` branch. The commit message includes `[skip ci]` to prevent triggering the workflow again.

---

### 9. **Job: Post-Merge Verification**

- **Purpose:**
  - Performs final verification steps after merging changes into the `main` branch to ensure stability and optionally deploys the application.
- **Trigger:**
  - **`if: github.ref == 'refs/heads/main' && github.event_name == 'push'`:** Only runs on pushes to the `main` branch.
- **Dependencies:**
  - **`needs: [lint, test, release, update-dev-version]`:** Ensures all previous jobs complete successfully before running post-merge verification.
- **Steps:**
  - **Check out code:** Retrieves the repository code.
  - **Set up Python:** Prepares the Python environment.
  - **Cache Dependencies:** Caches Poetry dependencies.
  - **Install Dependencies:** Installs Python dependencies via Poetry.
  - **Run critical post-merge checks:** Re-runs essential tests to confirm stability. Optionally, you can add deployment scripts here to deploy the application to production.
  - **Notify Deployment Success:** Sends a notification (e.g., Slack, Email) to inform the team that the deployment was successful.

---

## 🔍 Key Points and Best Practices

1. **Integrated Tag Validation:**
   - The **Tag Validation** job ensures that only tags created by the GitHub Actions bot are accepted. Unauthorized tags are automatically deleted, maintaining repository integrity.
2. **Dependency Caching:**
   - Caching Poetry and npm dependencies significantly reduces pipeline run times by avoiding redundant installations.
3. **Matrix Testing:**
   - Running tests across multiple Python versions ensures that your code is compatible and stable across different environments.
4. **Concurrency Control:**
   - Ensures that only the latest workflow run for a given branch or tag is active, optimizing resource usage and reducing potential conflicts.
5. **Pre-Commit Hooks (Optional but Recommended):**
   - While not directly part of the GitHub Actions workflow, implementing pre-commit hooks (using tools like `pre-commit`) can catch issues early in the development process, reducing pipeline failures.
6. **Secure Token Usage:**
   - The `GITHUB_TOKEN` is used securely within the workflow. Ensure that it has the necessary permissions (`contents: write`) to perform actions like deleting tags but follows the principle of least privilege.
7. **Artifact Uploads:**
   - Uploading coverage reports as artifacts allows for post-run analysis and tracking of code coverage over time.
8. **Notification Integration:**
   - Incorporating notification steps (e.g., Slack, Email) keeps the team informed about the status of deployments and pipeline runs.
9. **Modular Job Design:**
   - Each job has a clear purpose and dependencies, making the workflow easier to maintain and troubleshoot.

---

## 🚀 Next Steps

1. **Apply the Updated Workflow:**
   - Replace your existing `ci-cd.yml` with the updated version provided above in your repository's `.github/workflows/` directory.
2. **Configure Notification Action:**
   - Replace `some-notification-action@v1` with your preferred notification GitHub Action (e.g., Slack, Email). Ensure you have the necessary secrets configured for the notification service.
3. **Verify Permissions:**
   - Ensure that the `GITHUB_TOKEN` has the required permissions to delete tags. If not, adjust the workflow's permissions accordingly.
4. **Test the Workflow:**
   - Perform test runs by pushing commits, creating pull requests, and pushing tags to ensure that all jobs execute as expected and that tag validation works correctly.
5. **Implement Pre-Commit Hooks (Optional):**
   - Enhance code quality by setting up pre-commit hooks in your development environment. This step complements the CI/CD pipeline by catching issues early.
6. **Monitor and Iterate:**
   - Continuously monitor workflow runs, gather feedback from your team, and make iterative improvements to the pipeline as your project evolves.

---

## Deployment

Deploy the application using your preferred platform. The Dockerized setup simplifies deployment to platforms like AWS, GCP, DigitalOcean, or any other container-supported environment.

### Steps

1. **Build Docker Image**

   ```bash
   docker build -t qr-code-generator:latest .
   ```

2. **Push to Container Registry**

   ```bash
   docker tag qr-code-generator:latest yourregistry/qr-code-generator:latest
   docker push yourregistry/qr-code-generator:latest
   ```

3. **Deploy Using Docker Compose or Kubernetes**

   Use Docker Compose for simpler deployments or Kubernetes for more complex, scalable setups.

## Continuous Integration/Continuous Deployment (CI/CD)

Automate testing, building, and deployment using GitHub Actions or your preferred CI/CD platform.

### Example GitHub Actions Workflow

Refer to the [CI/CD Workflow for Python Backend](#cicd-workflow-for-python-backend) section above for a comprehensive `ci-cd.yml` configuration that includes tag validation, linting, testing, releasing, and post-merge verification.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   Ensure commits follow the [Commitlint](https://commitlint.js.org/) conventions.

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

   Provide a clear description of your changes and reference any related issues.

## License

This project is licensed under the [MIT License](LICENSE).

---

*This README was generated based on the project's current development plan. For the latest updates, please refer to the project's repository.*

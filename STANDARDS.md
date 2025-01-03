## 1. Type Hints and MyPy
```python
# Required
from typing import Optional, Any, Dict, List, Union, cast, Protocol

# Configuration (from pyproject.toml):
- Python version: 3.11
- Strict optional checks enabled
- No implicit optional
- Check untyped definitions
- Warn on redundant casts and unused ignores
- Pydantic plugin enabled

# Protocol Usage
class ServiceProtocol(Protocol):
    """Protocol defining service interface."""

    def method(self, param: str) -> Optional[Model]:
        """Method documentation."""
        ...

# Service Pattern
class Service:
    def __init__(self) -> None:
        """Initialize service."""
        self.db: Session

    def __call__(self, db: Session) -> "Service":
        """Make service callable with session."""
        self.db = db
        return self
```

## 2. Code Style (Black & Flake8)
```python
# Line Length
- Maximum line length: 88 characters (Black default)
- Use parentheses for line continuation
- Use trailing commas in multi-line structures

# Imports
- Group imports in this order:
  1. Standard library
  2. Third-party packages
  3. Local application imports
- Separate groups with a blank line
- No unused imports
- No * imports

# Naming Conventions
- Classes: PascalCase
- Functions/Variables: snake_case
- Constants: UPPER_SNAKE_CASE
- Private methods/variables: _leading_underscore
- Protocols: PascalCaseProtocol
```

## 3. Documentation
```python
# Docstrings (Google style)
def function_name(param1: type1, param2: type2) -> return_type:
    """Short description.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ExceptionType: Description of when this exception occurs
    """

# Protocol Documentation
class ServiceProtocol(Protocol):
    """Protocol defining service interface.

    All implementing classes must provide these methods
    with exact signatures and return types.
    """

    def method(self) -> None:
        """Method documentation.

        Must be implemented by concrete classes.
        """
        ...

# Class documentation
class ClassName:
    """Class description.

    Attributes:
        attr1: Description of attr1
        attr2: Description of attr2
    """
```

## 4. SQLAlchemy Patterns
```python
# Model Definitions
- Use explicit Column types
- Include nullable, default, index specifications
- Document all model attributes
- Use Enum for predefined choices

# Query Patterns
- Use select() over query() for new code
- Use type hints for model classes
- Cast SQLAlchemy Column types when needed
- Example: cast(str, model.column)

# Service Pattern
class UserService:
    def __init__(self) -> None:
        self.db: Session

    def __call__(self, db: Session) -> "UserService":
        self.db = db
        return self

    def get_by_id(self, id: int) -> Optional[Model]:
        return self.db.execute(
            select(Model).where(Model.id == id)
        ).scalar_one_or_none()
```

## 5. FastAPI Patterns
```python
# Route Definitions
- Use type hints for request/response models
- Document response status codes
- Include response_model in route decorators
- Use dependency injection for common operations

# Service Usage in Routes
@router.post("/")
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db)
) -> Item:
    """Create new item."""
    service = ItemService()(db)  # Initialize with session
    return service.create(item)

# Middleware
- Type hint request and response objects
- Document middleware effects

# Exception Handling
- Exception handlers must accept (Request, Exception) -> Response | Awaitable[Response]
- Use isinstance() to check specific exception types
- Re-raise unhandled exceptions
- Return JSONResponse with proper status codes and headers
- Include error type in response for better client handling

# Rate Limiting
- Use slowapi for rate limiting functionality
- Configure rate limits per endpoint or globally
- Include Retry-After headers in rate limit responses
- Disable rate limiting during tests using TESTING environment variable
- Handle rate limit exceptions with proper 429 status codes
```

## 6. Testing Standards
```python
# Test Structure
- Use descriptive test names
- Group related tests in classes
- Use fixtures for common setup
- Type hint test functions and fixtures
- Use Protocol types for service mocking

# Service Testing Pattern
@pytest.fixture
def service() -> ServiceProtocol:
    """Create service instance."""
    return Service()

def test_method(
    service: ServiceProtocol,
    db_session: Session
) -> None:
    """Test service method."""
    result = service(db_session).method()
    assert result is not None

# Test Documentation
def test_function_name(fixture1: Type1, fixture2: Type2) -> None:
    """Test description.

    Args:
        fixture1: Description of fixture1
        fixture2: Description of fixture2

    Tests:
        - Specific condition being tested
        - Expected outcome
    """
```

## 7. Version Control and Commits
```python
# Conventional Commits
<type>(<scope>): <description>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation only
- style: Code style changes
- refactor: Code refactoring
- perf: Performance improvements
- test: Adding/modifying tests
- chore: Maintenance tasks

Example:
feat(auth): add password reset functionality
```

## 8. Error Handling
```python
# Exception Patterns
- Use custom exception classes
- Document all possible exceptions
- Include context in error messages
- Use type hints for exception handlers

# Error Response Format
{
    "detail": "Human readable error message",
    "type": "error_type_identifier",
    "additional_info": "Optional context"
}

# Status Codes
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Validation Error
- 429: Rate Limit Exceeded
- 500: Internal Server Error
```

## 9. Security Practices
```python
# Security Rules
- No hardcoded secrets
- Use environment variables for configuration
- Hash passwords before storage
- Validate input data
- Use proper CORS settings
```

## 10. Project Structure
```
app/
├── core/          # Core functionality
├── models/        # Database models
├── schemas/       # Pydantic models
├── services/      # Business logic
├── routers/       # API routes
├── middleware/    # Custom middleware
└── utils/         # Utility functions

tests/             # Test files
├── conftest.py    # Test fixtures
└── test_*.py      # Test modules
```

## 11. Pre-commit Hooks
```yaml
# Configured hooks:
- black
- flake8
- mypy
- trailing whitespace
- end of files
- yaml check
- large files check
- merge conflicts
- private key detection
```

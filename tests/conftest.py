"""Test configuration and fixtures."""

import os
import time
from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text, URL
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.pool import NullPool

from app.main import app
from app.models.base import Base
from app.utils.db import get_db


def get_test_db_url(database: str = "postgres") -> URL:
    """Get test database URL."""
    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_pass = os.getenv("POSTGRES_PASSWORD", "postgres")
    db_host = os.getenv(
        "POSTGRES_HOST", "test-db" if os.getenv("DOCKER_ENV") == "1" else "localhost"
    )
    db_port = os.getenv("POSTGRES_PORT", "5432")

    return URL.create(
        "postgresql+psycopg2",
        username=db_user,
        password=db_pass,
        host=db_host,
        port=int(db_port),
        database=database,
    )


def wait_for_db(url: URL, timeout: int = 30, interval: int = 1) -> None:
    """Wait for database to be ready."""
    engine = create_engine(
        url,
        poolclass=NullPool,
        connect_args={"connect_timeout": 5, "options": "-c timezone=UTC"},
    )

    start_time = time.time()
    while True:
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
                break
        except OperationalError:
            if time.time() - start_time >= timeout:
                raise TimeoutError("Database connection timeout")
            time.sleep(interval)
        finally:
            engine.dispose()


def ensure_test_db() -> None:
    """Ensure test database exists."""
    engine = create_engine(
        get_test_db_url(), poolclass=NullPool, isolation_level="AUTOCOMMIT"
    )

    try:
        with engine.connect() as conn:
            # Check if test_db exists
            result = conn.execute(
                text("SELECT 1 FROM pg_database WHERE datname = 'test_db'")
            ).scalar()

            if not result:
                # Create test database if it doesn't exist
                conn.execute(text("CREATE DATABASE test_db"))
                conn.execute(
                    text("GRANT ALL PRIVILEGES ON DATABASE test_db TO postgres")
                )
    finally:
        engine.dispose()


@pytest.fixture(scope="session", autouse=True)
def setup_test_db() -> Generator[Session, None, None]:
    """Create test database and tables, then clean up after tests."""
    # Wait for the main postgres database to be ready
    wait_for_db(get_test_db_url())

    # Ensure test database exists
    ensure_test_db()

    # Wait for test database to be ready
    wait_for_db(get_test_db_url("test_db"))

    # Create engine for test database
    test_engine = create_engine(
        get_test_db_url("test_db"),
        poolclass=NullPool,
        connect_args={"connect_timeout": 10, "options": "-c timezone=UTC"},
    )

    try:
        # Create all tables
        Base.metadata.create_all(test_engine)

        # Create session factory
        TestingSessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=test_engine, expire_on_commit=False
        )

        # Create session
        session = TestingSessionLocal()

        yield session
    finally:
        session.close()
        Base.metadata.drop_all(test_engine)
        test_engine.dispose()


@pytest.fixture
def db_session(setup_test_db: Session) -> Generator[Session, None, None]:
    """Create a fresh database session for each test."""
    session = setup_test_db

    # Start transaction
    transaction = session.begin_nested()

    try:
        yield session
    finally:
        # Rollback transaction after each test
        if transaction.is_active:
            transaction.rollback()
        # Clear any remaining changes
        session.expire_all()


@pytest.fixture
def test_client(db_session: Session) -> Generator[TestClient, None, None]:
    """Create test client with database session."""

    def override_get_db() -> Generator[Session, None, None]:
        try:
            yield db_session
        except Exception:
            db_session.rollback()
            raise
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def setup_test_env() -> Generator[None, None, None]:
    """Set up test environment variables."""
    os.environ["TESTING"] = "1"
    yield
    os.environ["TESTING"] = "0"

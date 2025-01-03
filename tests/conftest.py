"""Test configuration and fixtures."""

import os
from typing import Any, Generator, Iterator
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
from pytest_postgresql import factories

from app.main import app
from app.models.base import Base
from app.utils.db import get_db


def load_database(**kwargs: dict[str, Any]) -> None:
    """Load initial database schema."""
    user = kwargs["user"]
    host = kwargs["host"]
    port = kwargs["port"]
    dbname = kwargs["dbname"]
    dsn = f"postgresql+psycopg2://{user}:@{host}:{port}/{dbname}"
    engine = create_engine(dsn)
    Base.metadata.create_all(engine)


# Create PostgreSQL fixtures for connecting to existing PostgreSQL instance
postgresql_my = factories.postgresql_noproc(
    host=os.getenv("POSTGRES_HOST", "127.0.0.1"),
    port=int(os.getenv("POSTGRES_PORT", "5432")),
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD", "postgres"),
    dbname=os.getenv("POSTGRES_DB", "test"),
)

postgresql = factories.postgresql("postgresql_my")


@pytest.fixture
def db_engine(postgresql: Any) -> Generator[Engine, None, None]:
    """Create database engine for testing."""
    dsn = (
        f"postgresql+psycopg2://{postgresql.info.user}:{postgresql.info.password}"
        f"@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}"
    )
    engine = create_engine(dsn)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture
def database_session(db_engine: Engine) -> Generator[Session, None, None]:
    """Create database session for testing."""
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = SessionLocal()

    try:
        yield session
    finally:
        # Clean up all tables after each test
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(text(f"TRUNCATE TABLE {table.name} CASCADE"))
        session.commit()
        session.close()


@pytest.fixture
def test_client(database_session: Session) -> TestClient:
    """Create test client with database session."""

    def override_get_db() -> Iterator[Session]:
        try:
            yield database_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


@pytest.fixture(autouse=True)
def setup_test_env() -> Generator[None, None, None]:
    """Set up test environment variables."""
    os.environ["TESTING"] = "1"
    yield
    os.environ["TESTING"] = "0"

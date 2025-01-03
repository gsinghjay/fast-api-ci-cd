"""Database utility functions."""

import os
import time
from typing import Generator, Optional
from sqlalchemy import create_engine, URL, Engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import OperationalError


def get_database_url() -> URL:
    """Get database URL based on environment variables."""
    db_user = os.getenv("POSTGRES_USER", "postgres")
    db_pass = os.getenv("POSTGRES_PASSWORD", "postgres")
    db_host = os.getenv(
        "POSTGRES_HOST", "test-db" if os.getenv("TESTING") == "1" else "localhost"
    )
    db_port = os.getenv("POSTGRES_PORT", "5432")
    db_name = os.getenv("POSTGRES_DB", "test_db")

    return URL.create(
        "postgresql+psycopg2",
        username=db_user,
        password=db_pass,
        host=db_host,
        port=int(db_port),
        database=db_name,
    )


def create_engine_with_retries(
    url: URL, max_retries: int = 5, retry_interval: int = 1
) -> Engine:
    """Create SQLAlchemy engine with connection retries."""
    engine = create_engine(
        url,
        poolclass=QueuePool,
        pool_size=5,
        max_overflow=10,
        pool_timeout=30,
        pool_pre_ping=True,
        pool_recycle=1800,  # Recycle connections after 30 minutes
        connect_args={
            "connect_timeout": 10,  # Connection timeout in seconds
            "options": "-c timezone=UTC",  # Set timezone at connection level
        },
    )

    # Try to establish initial connection
    for attempt in range(max_retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
                break
        except OperationalError:
            if attempt == max_retries - 1:
                raise
            time.sleep(retry_interval)

    return engine


# Get database URL from environment variable or use default
db_url_str: Optional[str] = os.getenv("DATABASE_URL")
DATABASE_URL: URL = URL.create(db_url_str) if db_url_str else get_database_url()

# Create engine with appropriate configuration
engine = create_engine_with_retries(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,  # Prevent expired object access issues
)


def get_db() -> Generator[Session, None, None]:
    """
    Get database session.

    Yields:
        Session: Database session

    Note:
        This function should be used as a FastAPI dependency
    """
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

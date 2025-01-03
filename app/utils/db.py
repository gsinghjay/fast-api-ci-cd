"""Database utility functions."""

import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Get database URL from environment variable or use default
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://test_user:test_password@localhost:5433/test_db"
)

# Create engine with appropriate connect_args
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # Only use check_same_thread for SQLite
    connect_args=(
        {}
        if SQLALCHEMY_DATABASE_URL.startswith("postgresql")
        else {"check_same_thread": False}
    ),
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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
    finally:
        db.close()

"""Create users table with authentication and authorization support.

Revision ID: 2e07b46d1878
Revises:
Create Date: 2025-01-02 23:15:05.612042

This migration creates the users table with the following features:
- Email-based authentication
- Password hashing
- Email verification
- Password reset functionality
- Role-based access control
- Timestamp tracking
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2e07b46d1878"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create users table with all necessary columns and constraints.

    Creates:
        - id: Primary key
        - email: Unique, indexed
        - full_name: Required
        - password: Hashed
        - is_verified: For email verification
        - role: For access control
        - verification_token: For email verification
        - password_reset_token: For password reset
        - password_reset_expires: Token expiration
        - last_login: Login tracking
        - created_at: Creation timestamp
        - updated_at: Update timestamp
    """
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=True),
        sa.Column("role", sa.String(length=50), nullable=False),
        sa.Column("verification_token", sa.String(), nullable=True),
        sa.Column("password_reset_token", sa.String(), nullable=True),
        sa.Column("password_reset_expires", sa.DateTime(), nullable=True),
        sa.Column("last_login", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)


def downgrade() -> None:
    """Remove users table and related indexes.

    This will:
    1. Drop the index on the id column
    2. Drop the users table
    """
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")

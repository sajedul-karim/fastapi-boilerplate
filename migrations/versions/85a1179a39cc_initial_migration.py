"""Initial migration

Revision ID: 85a1179a39cc
Revises: 
Create Date: 2024-02-28 19:36:10.023110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85a1179a39cc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the "users" table
    op.create_table(
        "user",  # Specify the table name
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("username", sa.String),
        sa.Column("email", sa.String),
        sa.Column("password", sa.String),
    )


def downgrade() -> None:
    # Drop the "users" table
    op.drop_table("user")

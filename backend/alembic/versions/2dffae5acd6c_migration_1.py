"""Migration 1

Revision ID: 2dffae5acd6c
Revises: 
Create Date: 2026-02-14 02:09:23.139805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision: str = '2dffae5acd6c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id",sa.String,primary_key=True),
        sa.Column("email",sa.String,unique=True),
        sa.Column("hashed_password",sa.String,nullable=True),
        sa.Column("full_name",sa.String,nullable=True),
        sa.Column("created_at",sa.DateTime,nullable=True),
        sa.Column("updated_at",sa.DateTime,nullable=True),
        sa.Column("is_active",sa.Boolean,nullable=True),
        sa.Column("preferences",JSONB,nullable=True)
    )
    op.create_table(
        "api_keys",
        sa.Column("id",sa.String,primary_key=True),
        sa.Column("user_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
        sa.Column("key_hash",sa.String,nullable=True),
        sa.Column("name",sa.String,nullable=True),
        sa.Column("created_at",sa.DateTime,nullable=True),
        sa.Column("updated_at",sa.DateTime,nullable=True),
        sa.Column("expires_at",sa.DateTime,nullable=True),
        sa.Column("is_active",sa.Boolean,nullable=True),
    )
    op.create_table(
        "projects",
        sa.Column("id",sa.String,primary_key=True),
        sa.Column("user_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
        sa.Column("name",sa.String,nullable=True),
        sa.Column("description",sa.String,nullable=True),
        sa.Column("created_at",sa.DateTime,nullable=True),
        sa.Column("updated_at",sa.DateTime,nullable=True),
        sa.Column("settings",sa.Boolean,nullable=True),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("api_keys")
    op.drop_table("projects")
    pass

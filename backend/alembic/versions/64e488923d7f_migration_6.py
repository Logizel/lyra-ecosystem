"""Migration 6

Revision ID: 64e488923d7f
Revises: e1b6ea8db4d1
Create Date: 2026-02-14 02:09:56.330227

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = '64e488923d7f'
down_revision: Union[str, Sequence[str], None] = 'e1b6ea8db4d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "knowledge_nodes",
    sa.Column("id",sa.String,primary_key=True),
    sa.Column("source_type",sa.String,sa.ForeignKey("users.id"),nullable=False),
    sa.Column("content",sa.String,nullable=True),
    sa.Column("metadata",JSONB,nullable=True),
    sa.Column("embedding", Vector(3), nullable=True),
    sa.Column("created_at",sa.DateTime,nullable=True),
    )
    op.create_table(
    "ideas",
    sa.Column("id",sa.String,primary_key=True),
    sa.Column("content",sa.String,nullable=True),
    sa.Column("created_by",sa.String,nullable=True),
    sa.Column("confidence",sa.Float, nullable=True),
    sa.Column("supporting_evidence",JSONB,nullable=True),
    sa.Column("created_at",sa.DateTime,nullable=True),
    )
    pass


def downgrade() -> None:
    op.drop_table("knowledge_nodes")
    op.drop_table("ideas")
    pass

"""Migration 2"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import JSONB, UUID
import uuid

revision: str = "e37b8a149260"
down_revision = "2dffae5acd6c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.create_table(
        "documents",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("project_id", UUID(as_uuid=True), sa.ForeignKey("projects.id", ondelete="CASCADE"), nullable=False),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("s3_path", sa.String),
        sa.Column("mime_type", sa.String),
        sa.Column("uploaded_at", sa.DateTime(timezone=True)),
        sa.Column("processed_at", sa.DateTime(timezone=True)),
        sa.Column("metadata", JSONB),
        sa.Column("total_chunks", sa.Integer),
    )

    op.create_table(
        "document_chunks",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("document_id", UUID(as_uuid=True), sa.ForeignKey("documents.id", ondelete="CASCADE"), nullable=False),
        sa.Column("chunk_index", sa.Integer),
        sa.Column("embedding", Vector(1536)),  # typical OpenAI size
        sa.Column("token_count", sa.Integer),
        sa.Column("metadata", JSONB),
    )


def downgrade() -> None:
    op.drop_table("document_chunks")
    op.drop_table("documents")

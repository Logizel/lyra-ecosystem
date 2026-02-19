"""Migration 2

Revision ID: e37b8a149260
Revises: 2dffae5acd6c
Create Date: 2026-02-14 02:09:33.429773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = 'e37b8a149260'
down_revision: Union[str, Sequence[str], None] = '2dffae5acd6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "documents",
    sa.Column("id",sa.String,primary_key=True),
    sa.Column("user_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
    sa.Column("project_id",sa.String,sa.ForeignKey("project.id"),nullable=False),
    sa.Column("s3_path",sa.String,nullable=True),
    sa.Column("mime_type",sa.String,nullable=True),
    sa.Column("uploaded_at",sa.DateTime,nullable=True),
    sa.Column("processed_at",sa.DateTime,nullable=True),
    sa.Column("metadata",JSONB,nullable=True), 
    sa.Column("total_chunks",sa.Integer,nullable=True),
    )   
    op.create_table(
    "document_chunks",
    sa.Column("id",sa.String,primary_key=True),
    sa.Column("document_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
    sa.Column("chunk_index",sa.Integer,nullable=True),
    sa.Column("embedding",Vector(3, float32),nullable=True),
    sa.Column("token_count",sa.Integer,nullable=True),
    sa.Column("metadata",JSONB,nullable=True)    
    )     
    pass


def downgrade() -> None:
    op.drop_table("documents")
    op.drop_table("document_chunks")
    pass

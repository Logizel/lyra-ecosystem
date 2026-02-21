"""Migration 5"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID
import uuid

revision: str = "e1b6ea8db4d1"
down_revision = "c7572c278c54"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "task_graph",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("project_id", UUID(as_uuid=True), sa.ForeignKey("projects.id", ondelete="CASCADE"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True)),
        sa.Column("status", sa.String(50)),
        sa.Column("metadata", JSONB),
    )

    op.create_table(
        "task_nodes",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("task_graph_id", UUID(as_uuid=True), sa.ForeignKey("task_graph.id", ondelete="CASCADE"), nullable=False),
        sa.Column("title", sa.String(255)),
        sa.Column("description", sa.String),
        sa.Column("status", sa.String(50)),
        sa.Column("order_index", sa.Integer),
        sa.Column("input_schema", JSONB),
        sa.Column("output_schema", JSONB),
        sa.Column("started_at", sa.DateTime(timezone=True)),
        sa.Column("completed_at", sa.DateTime(timezone=True)),
    )


def downgrade() -> None:
    op.drop_table("task_nodes")
    op.drop_table("task_graph")

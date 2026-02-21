"""Migration 4"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID
import uuid

revision: str = "c7572c278c54"
down_revision = "e8d99f424f80"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "agents",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("model_name", sa.String(255), nullable=False),
        sa.Column("version", sa.String(50)),
        sa.Column("last_updated", sa.DateTime(timezone=True)),
        sa.Column("configuration", JSONB),
    )

    op.create_table(
        "agent_runs",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("conversation_id", UUID(as_uuid=True), sa.ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False),
        sa.Column("agent_id", UUID(as_uuid=True), sa.ForeignKey("agents.id", ondelete="CASCADE"), nullable=False),
        sa.Column("input_data", JSONB),
        sa.Column("output_data", JSONB),
        sa.Column("tokens_used", sa.Integer),
        sa.Column("response_time", sa.Float),
        sa.Column("started_at", sa.DateTime(timezone=True)),
        sa.Column("completed_at", sa.DateTime(timezone=True)),
        sa.Column("status", sa.String(50)),
        sa.Column("error_message", sa.String),
    )

    op.create_table(
        "agent_feedback",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("agent_run_id", UUID(as_uuid=True), sa.ForeignKey("agent_runs.id", ondelete="CASCADE"), nullable=False),
        sa.Column("rating", sa.Integer),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("feedback_text", sa.Text),
    )


def downgrade() -> None:
    op.drop_table("agent_feedback")
    op.drop_table("agent_runs")
    op.drop_table("agents")

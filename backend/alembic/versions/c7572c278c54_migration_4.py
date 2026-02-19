"""Migration 4

Revision ID: c7572c278c54
Revises: e8d99f424f80
Create Date: 2026-02-14 02:09:43.732269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = 'c7572c278c54'
down_revision: Union[str, Sequence[str], None] = 'e8d99f424f80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "agents",
        sa.Column("model_name",sa.String,primary_key=True),
        sa.Column("version",sa.String,nullable=True),
        sa.Column("last_updated",sa.DateTime,nullable=True),
        sa.Column("configuration",JSONB,nullable=True)    
    )     
    op.create_table(
        "agent_feedback",
        sa.Column("id",sa.String,primary_key=True),
        sa.Column("agent_run_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
        sa.Column("user_id",sa.String,sa.ForeignKey("project.id"),nullable=False),
        sa.Column("rating",sa.Integer,nullable=True),
        sa.Column("created_at",sa.DateTime,nullable=True),
        sa.Column("feedback_text",sa.String,nullable=True),
    )
    op.create_table(
        "agent_runs",
        sa.Column("id",sa.String,primary_key=True),
        sa.Column("conversation_id",sa.String,sa.ForeignKey("conversation.id"),nullable=False),
        sa.Column("agent_type",sa.String,sa.ForeignKey("agent.type"),nullable=False),
        sa.Column("input_data",JSONB,nullable=True),
        sa.Column("output_data",JSONB,nullable=True),
        sa.Column("tokens_used",sa.Integer,nullable=True),
        sa.Column("response_time",sa.Float, nullable=True),
        sa.Column("started_at",sa.DateTime,nullable=True),
        sa.Column("completed_at",sa.DateTime,nullable=True),
        sa.Column("status",sa.String,nullable=True),
        sa.Column("error_message",sa.String,nullable=True),
    )
    pass


def downgrade() -> None:
    op.drop_table("agents")
    op.drop_table("agent_feedback")
    op.drop_table("agent_runs")

    pass

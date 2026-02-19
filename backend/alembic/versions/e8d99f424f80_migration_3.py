"""Migration 3

Revision ID: e8d99f424f80
Revises: e37b8a149260
Create Date: 2026-02-14 02:09:37.989094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = 'e8d99f424f80'
down_revision: Union[str, Sequence[str], None] = 'e37b8a149260'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "conversations",
    sa.Column("id",sa.String,primary_key=True),
    sa.Column("user_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
    sa.Column("project_id",sa.String,sa.ForeignKey("project.id"),nullable=False),
    sa.Column("title",sa.String,nullable=True),
    sa.Column("created_at",sa.DateTime,nullable=True),
    sa.Column("updated_at",sa.DateTime,nullable=True),
    sa.Column("context",JSONB,nullable=True), 
    sa.Column("status",sa.Integer,nullable=True),
    )     
    pass


def downgrade() -> None:
    op.create_table(
    "messages",
    sa.Column("id",sa.String,primary_key=True),
    sa.Column("conversation_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
    sa.Column("role",sa.String,nullable=True),
    sa.Column("context",sa.String,nullable=True),
    sa.Column("tokens_used",sa.Integer,nullable=True),
    sa.Column("model_used",sa.String,nullable=True),
    sa.Column("created_at",sa.DateTime,nullable=True),
    sa.Column("metadata",JSONB,nullable=True)    
    )     
 
    pass

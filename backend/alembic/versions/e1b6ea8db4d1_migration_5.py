"""Migration 5

Revision ID: e1b6ea8db4d1
Revises: c7572c278c54
Create Date: 2026-02-14 02:09:48.189657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB



# revision identifiers, used by Alembic.
revision: str = 'e1b6ea8db4d1'
down_revision: Union[str, Sequence[str], None] = 'c7572c278c54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "task_nodes",
    sa.Column("id",sa.String,primary_key=True),
    sa.Column("task_graph_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
    sa.Column("title",sa.String,nullable=True),
    sa.Column("description",sa.String,nullable=True),
    sa.Column("status",sa.String,nullable=True),
    sa.Column("order_index",sa.Integer,nullable=True),
    sa.Column("input_schema",JSONB,nullable=True),
    sa.Column("output_schema",JSONB,nullable=True),
    sa.Column("started_at",sa.DateTime,nullable=True),
    sa.Column("completed_at",sa.DateTime,nullable=True),
    )
    op.create_table(
    "task_graph",
    sa.Column("id",sa.String,primary_key=True),
    sa.Column("project_id",sa.String,sa.ForeignKey("users.id"),nullable=False),
    sa.Column("created_at",sa.DateTime,nullable=True),
    sa.Column("updated_at",sa.DateTime,nullable=True),
    sa.Column("status",sa.String,nullable=True),
    sa.Column("metadata",JSONB,nullable=True)
    )
    pass


def downgrade() -> None:
    op.drop_table("task_nodes")
    op.drop_table("task_graph")
 
    pass

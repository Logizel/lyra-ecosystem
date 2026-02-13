"""Migration 2

Revision ID: e37b8a149260
Revises: 2dffae5acd6c
Create Date: 2026-02-14 02:09:33.429773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e37b8a149260'
down_revision: Union[str, Sequence[str], None] = '2dffae5acd6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

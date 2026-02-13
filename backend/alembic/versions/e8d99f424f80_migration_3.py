"""Migration 3

Revision ID: e8d99f424f80
Revises: e37b8a149260
Create Date: 2026-02-14 02:09:37.989094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8d99f424f80'
down_revision: Union[str, Sequence[str], None] = 'e37b8a149260'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

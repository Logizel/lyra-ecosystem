"""Migration 6

Revision ID: 64e488923d7f
Revises: e1b6ea8db4d1
Create Date: 2026-02-14 02:09:56.330227

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64e488923d7f'
down_revision: Union[str, Sequence[str], None] = 'e1b6ea8db4d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

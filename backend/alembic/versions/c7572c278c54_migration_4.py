"""Migration 4

Revision ID: c7572c278c54
Revises: e8d99f424f80
Create Date: 2026-02-14 02:09:43.732269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7572c278c54'
down_revision: Union[str, Sequence[str], None] = 'e8d99f424f80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

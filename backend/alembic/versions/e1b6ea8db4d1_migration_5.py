"""Migration 5

Revision ID: e1b6ea8db4d1
Revises: c7572c278c54
Create Date: 2026-02-14 02:09:48.189657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1b6ea8db4d1'
down_revision: Union[str, Sequence[str], None] = 'c7572c278c54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

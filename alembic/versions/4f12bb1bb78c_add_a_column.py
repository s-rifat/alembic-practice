"""Add a column

Revision ID: 4f12bb1bb78c
Revises: 2c3afdf49131
Create Date: 2026-01-22 12:32:29.999578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f12bb1bb78c'
down_revision: Union[str, Sequence[str], None] = '2c3afdf49131'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('account') as batch_op:
        batch_op.drop_column('last_transaction_date')

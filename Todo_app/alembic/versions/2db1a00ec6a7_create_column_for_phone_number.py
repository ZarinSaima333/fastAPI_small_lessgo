"""create column for phone number

Revision ID: 2db1a00ec6a7
Revises: 
Create Date: 2026-01-05 15:20:39.876348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2db1a00ec6a7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))
    pass
# def upgrade() -> None:
#     """Upgrade schema."""
#     pass


def downgrade() -> None:
    op.drop_column('users','phone_number')

#cmd: alembic downgrade -1 (revert the last upgrade)
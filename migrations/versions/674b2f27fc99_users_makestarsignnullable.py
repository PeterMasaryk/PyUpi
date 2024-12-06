"""Users_MakeStarSignNullable

Revision ID: 674b2f27fc99
Revises: 577cb83946c8
Create Date: 2024-12-06 14:13:48.175578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '674b2f27fc99'
down_revision: Union[str, None] = '577cb83946c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'star_sign',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.alter_column('users', 'star_sign',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
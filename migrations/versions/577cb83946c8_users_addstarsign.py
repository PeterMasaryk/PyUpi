"""Users_AddStarSign

Revision ID: 577cb83946c8
Revises: 36e2bafc3b97
Create Date: 2024-12-05 23:58:21.831264

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "577cb83946c8"
down_revision: Union[str, None] = "36e2bafc3b97"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("star_sign", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "star_sign")
    # ### end Alembic commands ###

"""added trusted field to worker

Revision ID: 486fe9e7fb84
Revises: 23651ab20341
Create Date: 2023-03-08 22:56:52.871106

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "486fe9e7fb84"
down_revision = "23651ab20341"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("worker", sa.Column("trusted", sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("worker", "trusted")
    # ### end Alembic commands ###
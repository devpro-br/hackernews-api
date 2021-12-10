"""Adiciona User.password

Revision ID: 4bd7bc7e514b
Revises: 9590c8bed039
Create Date: 2021-12-10 14:22:12.584148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4bd7bc7e514b"
down_revision = "9590c8bed039"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("password", sa.String(length=128), nullable=True))


def downgrade():
    op.drop_column("users", "password")

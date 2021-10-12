"""Cria tabela de usuários

Revision ID: e608b0a91508
Revises: 
Create Date: 2021-10-12 00:28:16.314562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e608b0a91508"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=128), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("avatar", sa.UnicodeText(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )


def downgrade():
    op.drop_table("users")

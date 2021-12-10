from datetime import datetime, timezone
import sqlalchemy as sa

from hackernews.ext.database import db


class User(db.Model):

    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(128), unique=True, nullable=False)
    password = sa.Column(sa.String(128), nullable=True)
    email = sa.Column(sa.String(255), unique=True, nullable=True)
    name = sa.Column(sa.String(128), nullable=False)
    avatar = sa.Column(sa.UnicodeText(), nullable=True)
    created_at = sa.Column(
        sa.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return self.name

    def to_dict(self):
        """Convert model to dict"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "avatar": self.avatar,
            "created_at": self.created_at.isoformat(),
        }

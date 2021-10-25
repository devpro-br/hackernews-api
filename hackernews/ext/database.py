from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_app(app):
    """Initialize the database & migrations"""
    db.init_app(app)
    migrate.init_app(app, db)

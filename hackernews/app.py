from hackernews.ext import configuration, api, database
from hackernews.models.users import User  # pylint: disable=W0611
from hackernews.models.news import News  # pylint: disable=W0611


def create_app(**config):
    """Cria flask app"""
    app = api.create_api_app()
    configuration.init_app(app, **config)
    database.init_app(app)
    return app

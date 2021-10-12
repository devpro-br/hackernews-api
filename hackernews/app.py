from hackernews.ext import configuration, api, database


def create_app(**config):
    """Cria flask app"""
    app = api.create_api_app()
    configuration.init_app(app, **config)
    database.init_app(app)
    return app

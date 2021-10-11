from hackernews.ext import configuration, api


def create_app(**config):
    """Cria flask app"""
    app = api.create_api_app()
    configuration.init_app(app, **config)
    return app

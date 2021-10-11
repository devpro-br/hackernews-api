from hackernews.ext import configuration, api


def create_app(**config):
    app = api.create_api_app()
    configuration.init_app(app, **config)
    return app

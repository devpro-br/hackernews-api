import os


def init_app(app):
    """Flask init app"""
    config = get_config_from_env()
    app.config.from_object(config)


def get_config_from_env():
    """Carrega configurações do ambiente"""
    envname = os.getenv("FLASK_ENV", "production").lower()
    if envname == "development":
        return DevelopmentConfig()
    return ProductionConfig()


class ProductionConfig:  # pylint: disable=R0903
    """PROD"""

    # FLASK
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "Ch@nG3_th1s_IN_PR0D!")

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AUTH and JWT
    JWT_ISS = os.getenv("JWT_ISS", "https://confrarianews.com.br")
    JWT_AUD = os.getenv("JWT_AUD", "auth.confrarianews.com.br")
    JWT_EXPIRE_DAYS = int(os.getenv("JWT_EXPIRE_DAYS", "30"))
    JWT_EXPIRE_HOURS = int(os.getenv("JWT_EXPIRE_HOURS", "0"))
    JWT_RTOKEN_EXPIRE_DAYS = int(os.getenv("JWT_RTOKEN_EXPIRE_DAYS", "180"))


class DevelopmentConfig(ProductionConfig):  # pylint: disable=R0903
    """DEV"""

    FLASK_ENV = "development"
    DEBUG = True

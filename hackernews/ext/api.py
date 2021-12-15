import connexion
from flask_cors import CORS

from hackernews.exceptions import ConflictValueException, UnauthorizedException


def not_authorized_handler(error):
    """Convert erros de serviços em erros de API"""
    return {
        "detail": str(error),
        "status": 401,
        "title": "Unauthorized Request",
    }, 401


def data_conflict_handler(error):
    """Convert erros de serviços em erros de API"""
    return {
        "detail": str(error),
        "status": 409,
        "title": "Data Conflict Request",
    }, 409


def create_api_app(version="/"):
    """Cria flask app via Connexion (OpenAPI 3)"""
    connexion_app = connexion.FlaskApp(
        __name__,
        specification_dir="../api/",
        options={
            "swagger_url": "api",
        },
    )
    connexion_app.add_api("openapi.yaml", validate_responses=True, base_path=version)

    # CORS
    CORS(connexion_app.app)

    # Error handlers
    connexion_app.add_error_handler(UnauthorizedException, not_authorized_handler)
    connexion_app.add_error_handler(ConflictValueException, data_conflict_handler)

    return connexion_app.app

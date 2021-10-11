import connexion


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
    return connexion_app.app

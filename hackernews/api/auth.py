from flask import jsonify
from hackernews.services import auth as auth_services


def login(body):
    """
    Login do usuário retornando token
    """
    return auth_services.login(body["username"], body["password"])


def signup(body):
    """
    Registra um novo usuário
    """
    new_login = auth_services.create_user(
        body["username"],
        body["password"],
        body["email"],
        body["name"],
        body.get("avatar"),
    )
    return jsonify(new_login), 201

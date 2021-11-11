from hackernews.services import auth as auth_services


def login(body):
    """
    Login do usuário retornando token
    """
    return auth_services.login(body["username"], body["password"])

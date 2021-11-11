from hackernews.exceptions import UnauthorizedException
from hackernews.services import token as token_services
from hackernews.models.users import User


def _generate_user_login_tokens(user):
    """
    gera par de tokens
    """
    token = token_services.generate_token(user)
    refresh_token = token_services.generate_refresh_token(user)
    return {
        "token": token,
        "refresh_token": refresh_token,
    }


def login(username, password):
    """
    versão inicial do login
    TODO: validar de verdade password ou usar OAUTH
    """
    error_msg = "Username or password invalid"
    if not password == username:
        raise UnauthorizedException(error_msg)

    user = User.query.filter_by(username=username).first()
    if not user:
        raise UnauthorizedException(error_msg)

    return _generate_user_login_tokens(user)

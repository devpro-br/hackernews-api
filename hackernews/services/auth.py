from werkzeug.security import check_password_hash, generate_password_hash

from hackernews.ext.database import db
from hackernews.exceptions import (
    UnauthorizedException,
    InvalidValueException,
    ConflictValueException,
)
from hackernews.services import token as token_services
from hackernews.models.users import User

INVALID_LOGIN_MSG = "Username or password invalid"


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
    user = User.query.filter_by(username=username).first()
    if not user:
        raise UnauthorizedException(INVALID_LOGIN_MSG)

    valid_password = check_password_hash(user.password, password)
    if not valid_password:
        raise UnauthorizedException(INVALID_LOGIN_MSG)

    return _generate_user_login_tokens(user)


def create_user(username, password, email, name, avatar=None):
    """
    Cria novo usuário
    """

    if not username:
        raise InvalidValueException("Invalid username")

    if not email:
        raise InvalidValueException("Invalid email")

    if not password:
        raise InvalidValueException("Invalid password")

    if User.query.filter(User.email == email).first():
        raise ConflictValueException(f"E-Mail '{email}' already taken.")

    if User.query.filter(User.username == username).first():
        raise ConflictValueException(f"Username '{username}' already taken.")

    new_user = User(
        username=username,
        password=generate_password_hash(password),
        email=email,
        name=name,
        avatar=avatar,
    )
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict()

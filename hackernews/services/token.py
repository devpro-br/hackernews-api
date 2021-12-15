from datetime import datetime, timedelta, timezone

import jwt
from flask import current_app

from hackernews.exceptions import UnauthorizedException


def generate_token(user, days=None, hours=None, scope=None):
    """
    Gera token
    """
    if not scope:
        scope = ["news:create"]

    if days is None:
        days = current_app.config["JWT_EXPIRE_DAYS"]
    if hours is None:
        hours = current_app.config["JWT_EXPIRE_HOURS"]

    token_expiration = datetime.now(timezone.utc) + timedelta(days=days, hours=hours)
    return jwt.encode(
        {
            "iss": current_app.config["JWT_ISS"],
            "aud": current_app.config["JWT_AUD"],
            "exp": token_expiration,
            "expire_date": token_expiration.isoformat(),
            "sub": user.id,
            "username": user.username,
            "email": user.email,
            "name": user.name,
            "avatar": user.avatar,
            "scope": scope,
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256",
    )


def generate_refresh_token(user):
    """
    Generates a long term token with only the refresh token permission (scope)
    """
    days = current_app.config["JWT_RTOKEN_EXPIRE_DAYS"]
    return generate_token(user, days=days, hours=0, scope=["auth:refresh_token"])


def check_token_info(token):
    """
    valida token das requisições
    """
    # pylint: disable=W0707
    try:
        token_info = jwt.decode(
            jwt=token,
            key=current_app.config["SECRET_KEY"],
            issuer=current_app.config["JWT_ISS"],
            audience=current_app.config["JWT_AUD"],
            algorithms=["HS256"],
        )
        return token_info

    except jwt.ExpiredSignatureError as error:
        raise UnauthorizedException(f"Expired token: {str(error)}")
    except Exception as error:
        raise UnauthorizedException(f"Invalid token: {str(error)}")

import pytest
from werkzeug.security import generate_password_hash

from hackernews.exceptions import UnauthorizedException
from hackernews.services import auth
from hackernews.models.users import User


def test_should_return_wrong_login_message():
    """
    Teste deve retornar exception se nao existe o usuário
    ou a senha incorreta
    """
    with pytest.raises(UnauthorizedException) as error:
        auth.login(username="invalid", password="bla")

    assert str(error.value) == "Username or password invalid"


def test_should_return_tokens(db_session):
    """
    Teste deve retornar usuário quando a senha está correta
    """
    user = User(
        name="John Doe",
        username="jd@example.com",
        email="jd@example.com",
        password=generate_password_hash("abacate"),
    )
    db_session.add(user)
    db_session.commit()

    response = auth.login("jd@example.com", "abacate")

    assert response["token"] is not None
    assert response["refresh_token"] is not None


def test_should_return_return_invalid_login_msg(db_session):
    """
    Teste deve retornar usuário quando a senha está correta
    """
    user = User(
        name="John Doe",
        username="jd",
        email="jd@example.com",
    )
    db_session.add(user)
    db_session.commit()

    with pytest.raises(UnauthorizedException) as error:
        auth.login(username="invalid", password="bla")

    assert str(error.value) == "Username or password invalid"

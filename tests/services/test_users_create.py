import pytest
from unittest.mock import ANY

from hackernews.exceptions import (
    ConflictValueException,
    UnauthorizedException,
    InvalidValueException,
)
from hackernews.services import auth
from hackernews.models.users import User


def test_should_create_user():
    """
    Teste deve criar novo usuário
    """
    user = auth.create_user(
        username="jd",
        password="abc",
        email="jd@example.com",
        name="John Doe",
    )

    assert user == {
        "id": ANY,
        "username": "jd",
        "email": "jd@example.com",
        "name": "John Doe",
        "avatar": None,
        "created_at": ANY,
    }


def test_should_not_create_empty_username():
    """
    Teste nao deve aceitar criar usuário sem username
    """
    with pytest.raises(InvalidValueException) as error:
        auth.create_user(
            username=None,
            password="abc",
            email="jd@example.com",
            name="John Doe",
        )

    assert str(error.value) == "Invalid username"


def test_should_not_create_empty_email():
    """
    Teste nao deve aceitar criar usuário sem email
    """
    with pytest.raises(InvalidValueException) as error:
        auth.create_user(
            username="jd",
            password="abc",
            email=None,
            name="John Doe",
        )

    assert str(error.value) == "Invalid email"


def test_should_not_create_duplicated_username(db_session):

    user = User(
        username="jd",
        password="abc",
        email="jd@example.com",
        name="John Doe",
    )
    db_session.add(user)
    db_session.commit()

    with pytest.raises(ConflictValueException) as error:
        auth.create_user(
            username="jd",
            password="abc",
            email="jd@example.com",
            name="John Doe",
        )

    assert str(error.value) == "E-Mail 'jd@example.com' already taken."


def test_should_create_user_with_no_password():
    """
    Teste deve criar novo usuário
    """
    with pytest.raises(InvalidValueException) as error:
        auth.create_user(
            username="jd",
            password="",
            email="jd@example.com",
            name="John Doe",
        )

    assert str(error.value) == "Invalid password"

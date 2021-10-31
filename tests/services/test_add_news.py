import pytest
from unittest.mock import ANY

from hackernews.services import news as news_services


def test_should_not_create_news_without_title():

    with pytest.raises(ValueError) as error:
        news_services.create_news(title=None)

    assert str(error.value) == "Invalid title"


def test_should_add_news_using_just_title():
    new_item = news_services.create_news(title="Simple Title")

    assert new_item["id"] is not None
    assert new_item["created_at"] is not None
    assert new_item["title"] == "Simple Title"

    # TODO: Logo nao devemos aceitar criar news sem um Author
    assert new_item["author"] is None


def test_should_create_a_complete_news(user_mock):
    new_item = news_services.create_news(
        title="The very first news",
        description="This is the first news...",
        author_id=user_mock.id,
    )

    assert new_item == {
        "author": {
            "avatar": user_mock.avatar,
            "created_at": ANY,
            "email": user_mock.email,
            "id": user_mock.id,
            "name": user_mock.name,
            "username": user_mock.username,
        },
        "created_at": ANY,
        "description": "This is the first news...",
        "id": ANY,
        "title": "The very first news",
    }


def test_should_not_accept_long_titles(db_session):
    # Given an long title
    long_title = "L" * 130

    # When the title is invalid
    with pytest.raises(ValueError) as error:
        news_services.create_news(title=long_title)

    # Then
    assert str(error.value) == "Title is too long"

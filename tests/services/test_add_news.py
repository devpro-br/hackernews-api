from unittest.mock import ANY
from hackernews.models.news import News
from hackernews.services import news as news_services


def test_should_add_news(db_session, user_mock):
    # Given a Tabnews
    the_news = News(
        title="The very first news",
        description="This is the first news...",
        author_id=user_mock.id,
    )
    db_session.add(the_news)
    db_session.commit()

    # Then
    assert the_news.to_dict() == {
        "author": {
            "avatar": user_mock.avatar,
            "created_at": ANY,
            "email": user_mock.email,
            "id": user_mock.id,
            "name": user_mock.name,
            "username": "jd",
        },
        "created_at": ANY,
        "description": "This is the first news...",
        "id": ANY,
        "title": "The very first news",
    }

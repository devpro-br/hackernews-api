from mock import patch


def test_should_return_bad_request(token_valid_mock, client):
    # Given a request with no input data (body)
    response = client.post(
        "/api/news", headers={"authorization": f"Bearer {token_valid_mock}"}
    )

    # Then
    assert response.status_code == 400
    assert response.json["detail"] == "None is not of type 'object'"


def test_should_return_title_is_a_required_field(token_valid_mock, client):
    # Given a request with a missing required field
    response = client.post(
        "/api/news",
        headers={"authorization": f"Bearer {token_valid_mock}"},
        json={},
    )

    # Then
    assert response.status_code == 400
    assert response.json["detail"] == "'title' is a required property"


def test_should_reject_title_less_than_min_title_length(token_valid_mock, client):
    # Given a request with an invalid title
    response = client.post(
        "/api/news",
        headers={"authorization": f"Bearer {token_valid_mock}"},
        json={"title": "tiny-title"},
    )

    # Then
    assert response.status_code == 400
    assert response.json["detail"] == "'tiny-title' is too short - 'title'"


@patch("hackernews.services.news.create_news")
def test_should_accept_null_description(news_mock, token_valid_mock, client):

    news_mock.return_value = {}

    # Given a request with an empty description (non string)
    response = client.post(
        "/api/news",
        headers={"authorization": f"Bearer {token_valid_mock}"},
        json={
            "title": "A valid and simple title",
            "description": None,
        },
    )

    # Then
    assert response.status_code == 201
    news_mock.assert_called_once_with("A valid and simple title", None)


@patch("hackernews.services.news.create_news")
def test_create_news_id(news_mock, token_valid_mock, client):

    news_mock.return_value = {}

    response = client.post(
        "/api/news",
        headers={"authorization": f"Bearer {token_valid_mock}"},
        json={
            "title": "First Test News",
            "description": "1o. teste",
        },
    )

    assert response.status_code == 201
    news_mock.assert_called_once_with("First Test News", "1o. teste")

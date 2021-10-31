def test_should_return_bad_request(client):
    # Given a request with no input data (body)
    response = client.post(
        "/api/news",
    )

    # Then
    assert response.status_code == 400
    assert response.json["detail"] == "None is not of type 'object'"


def test_should_return_title_is_a_required_field(client):
    # Given a request with a missing required field
    response = client.post(
        "/api/news",
        json={},
    )

    # Then
    assert response.status_code == 400
    assert response.json["detail"] == "'title' is a required property"


def test_should_reject_title_less_than_min_title_length(client):
    # Given a request with an invalid title
    response = client.post(
        "/api/news",
        json={"title": "tiny-title"},
    )

    # Then
    assert response.status_code == 400
    assert response.json["detail"] == "'tiny-title' is too short - 'title'"


def test_should_accept_null_description(client):
    # Given a request with an empty description (non string)
    response = client.post(
        "/api/news",
        json={
            "title": "A valid and simple title",
            "description": None,
        },
    )

    # Then
    assert response.status_code == 201


def test_create_news_id(client):
    response = client.post(
        "/api/news",
        json={
            "title": "First Test News",
            "description": "1o. teste",
        },
    )
    news = response.json

    assert news.get("id") is not None


def test_create_news_status_created(client):
    response = client.post(
        "/api/news",
        json={
            "title": "First Test News",
            "description": "1o. teste",
        },
    )

    assert response.status_code == 201

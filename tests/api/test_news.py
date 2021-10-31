def test_create_news_id(client):
    response = client.post(
        "/api/news",
        json={
            "title": "First Test News",
            "description": "1o. teste",
        },
    )
    news = response.json

    assert news.get("id") == 1


def test_create_news_status_created(client):
    response = client.post(
        "/api/news",
        json={
            "title": "First Test News",
            "description": "1o. teste",
        },
    )

    assert response.status_code == 201

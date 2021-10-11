def test_should_return_not_found(client):

    response = client.get("/api/invalid/url")

    assert response.status_code == 404


def test_should_get_the_list_news(client):

    response = client.get(
        "/api/news",
        headers={"content-type": "application/json"},
    )

    assert response.status_code == 200

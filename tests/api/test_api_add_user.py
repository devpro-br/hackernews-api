from mock import patch


@patch("hackernews.services.auth.create_user")
def test_should_create_new_user(create_user_mock, client):

    create_user_mock.return_value = {}

    # Given a request with an empty description (non string)
    response = client.post(
        "/api/auth/signup",
        json={
            "username": "jd@example.com",
            "password": "abc",
            "email": "jd@example.com",
            "name": "John Doe",
        },
    )

    # Then
    assert response.status_code == 201
    create_user_mock.assert_called_once_with(
        "jd@example.com",
        "abc",
        "jd@example.com",
        "John Doe",
        None,
    )


@patch("hackernews.services.auth.create_user")
def test_should_return_bad_request(create_user_mock, client):

    create_user_mock.return_value = {}

    # Given a request with an empty description (non string)
    response = client.post(
        "/api/auth/signup",
        json={
            "email": "jd@example.com",
        },
    )

    # Then
    assert response.status_code == 400
    assert response.json["detail"] == "'username' is a required property"

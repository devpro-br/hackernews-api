import mock

from hackernews.exceptions import UnauthorizedException


def test_should_return_bad_request_when_there_is_no_body(client):
    """
    Teste tem que retornar 400 quando nao é enviado email/password no body
    """
    response = client.post(
        "/api/auth/login",
        headers={"content-type": "application/json"},
    )
    assert response.status_code == 400
    assert response.json["detail"] == "None is not of type 'object'"


@mock.patch("hackernews.services.auth.login")
def test_should_return_tokens(auth_mock, client):
    """
    Teste tem que retornar os dados do usuário,
    um token e um refresh_token
    """

    auth_mock.return_value = {
        "token": "abcd",
        "refresh_token": "abcd",
    }

    response = client.post(
        "/api/auth/login",
        headers={"content-type": "application/json"},
        json={
            "username": "jd",
            "password": "abacate",
        },
    )

    auth_mock.assert_called_once_with("jd", "abacate")

    assert response.status_code == 200
    assert response.json["token"] is not None
    assert response.json["refresh_token"] is not None


def test_should_return_invalid_login(client):
    """
    Teste tem que retornar 401 quando o service retorna erro
    """

    with mock.patch("hackernews.services.auth.login") as auth_mock:
        auth_mock.side_effect = UnauthorizedException("Username or password invalid")

        response = client.post(
            "/api/auth/login",
            headers={"content-type": "application/json"},
            json={
                "username": "jd",
                "password": "invalid-pwd",
            },
        )

    assert response.status_code == 401
    assert response.json["detail"] == "Username or password invalid"

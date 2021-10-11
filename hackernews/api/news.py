from flask import jsonify


def list_news():
    news = [
        {
            "author": {
                "avatar": "http://example.com/img/avatar/jose_thumb.png",
                "id": 1,
                "name": "John Doe",
            },
            "created_at": "2021-01-11T11:32:28+00:00",
            "description": "string",
            "id": 42,
            "title": "Python is a great option for backend and APIs",
        }
    ]
    return jsonify(news)

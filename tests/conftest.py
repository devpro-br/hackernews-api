import pytest

from hackernews.app import create_app


@pytest.fixture(autouse=False)
def app():
    app = create_app()
    with app.app_context():
        yield app

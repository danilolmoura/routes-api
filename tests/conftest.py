import pytest

from application import create_app

@pytest.fixture(scope='session', autouse=True)
def app():
    app = create_app('test')
    return app


@pytest.fixture(scope='function', autouse=True)
def test_client(app):
    return app.test_client()

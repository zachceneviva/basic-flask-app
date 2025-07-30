from flask.testing import FlaskClient
from flask import Flask
import pytest
from app import app as flask_app


@pytest.fixture
def app() -> Flask:
    yield flask_app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_hello_world(client: FlaskClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"

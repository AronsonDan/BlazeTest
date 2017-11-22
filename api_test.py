import json
import pytest
from api import app

url = '/qa_test/api/v1.0/user'


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))


def test_get_names(client):
    response = client.get(url)
    data = json_of_response(response)

    assert response.status_code == 200
    assert data["firstName"] == 'API'
    assert data["lastName"] == 'Tester'


def test_patch_names(client):
    response = client.patch(url)
    data = json_of_response(response)

    assert response.status_code == 200
    assert data["firstName"] == 'ABC'
    assert data["lastName"] == 'XYZ'


def test_post_names(client):
    response = client.post(url)
    data = json_of_response(response)

    assert response.status_code == 200
    assert data["firstName"] == 'API'
    assert data["lastName"] == 'Tester'

import json


def test_create_user(client):
    data = {
        "username": "testuser",
        "email": "testuser@foobar.com",
        "password": "testing",
    }
    response = client.post("/users/", content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@foobar.com"
    assert response.json()["is_active"] is True

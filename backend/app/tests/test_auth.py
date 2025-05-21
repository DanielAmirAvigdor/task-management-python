import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.fixture(scope="module")
def registered_user():
    # Use a consistent email address
    email = "fixture@example.com"
    password = "Password1"

    # Register a test user
    res = client.post("/auth/register", json={
        "email": email,
        "password": password,
        "first_name": "Test",
        "last_name": "User"
    })
    print("REGISTER RESPONSE JSON:", res.json())
    assert res.status_code == 200

    return {
        "email": email,
        "password": password
    }


# def test_register_user():
#     res = client.post("/auth/register", json={
#         "email": "user@example.com",
#         "password": "Password1",
#         "first_name": "User",
#         "last_name": "Example"
#     })
#     assert res.status_code == 200
#     assert res.json()["email"] == "user@example.com"


def test_register_existing_email(registered_user):
    res = client.post("/auth/register", json={
        "email": registered_user["email"],
        "password": "Password1",
        "first_name": "Another",
        "last_name": "User"
    })
    assert res.status_code == 400
    assert res.json()["detail"] == "Email already registered"


def test_login_success(registered_user):
    res = client.post("/auth/login", data={
        "username": registered_user["email"],
        "password": registered_user["password"]
    })
    assert res.status_code == 200
    json_data = res.json()
    assert "access_token" in json_data
    assert json_data["token_type"] == "bearer"
    assert res.json()["user"]["email"] == registered_user["email"]


def test_login_invalid_password(registered_user):
    res = client.post("/auth/login", data={
        "username": registered_user["email"],
        "password": "WrongPassword1"
    })
    assert res.status_code == 401
    assert res.json()["detail"] == "Incorrect email or password"


def test_login_unregistered_email():
    res = client.post("/auth/login", data={
        "username": "nonexistent@example.com",
        "password": "Whatever123"
    })
    assert res.status_code == 401
    assert res.json()["detail"] == "Incorrect email or password"

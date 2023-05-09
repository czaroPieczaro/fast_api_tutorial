from db.repository.login import get_user
from db.repository.users import create_new_user
from fastapi.testclient import TestClient
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def user_authentication_headers(client: TestClient, username: str, password: str):
    data = {"username": username, "password": password}
    r = client.post("/login/token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_username(client: TestClient, username: str, db: Session):
    """
    Return a valid token for the user with username provided. If user doesn't exist, create first.
    """
    password = "test_password"
    email = "test_email@email.com"
    user = get_user(username=username, db=db)
    if not user:
        user_in_create = UserCreate(username=username, email=email, password=password)
        create_new_user(user_in_create, db=db)
    return user_authentication_headers(client, username, password)

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database import SessionLocal, engine
from src.models import Base
from sqlalchemy import create_engine

@pytest.fixture(scope="module")
def test_client():
    # Set up the database and create tables
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    # Teardown
    Base.metadata.drop_all(bind=engine)

def test_create_contact(test_client: TestClient):
    response = test_client.post("/contacts/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone_number": "1234567890"
    })
    assert response.status_code == 201
    assert response.json()["first_name"] == "John"

def test_read_contact(test_client: TestClient):
    response = test_client.get("/contacts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

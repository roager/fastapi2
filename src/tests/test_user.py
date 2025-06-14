import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    # Aquí abrimos el TestClient **tras** la inicialización de la DB
    with TestClient(app) as c:
        yield c

def test_root(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "¡Hola, mundo!!!!!"}

def test_ping(client):
    r = client.get("/ping")
    assert r.status_code == 200
    assert r.json() == {"message": "pong"}

# def test_create_and_list_user(client):
#     # 1. Crear usuario
#     r = client.post("/users/", json={"name": "Ana", "email": "ana@example.com"})
#     assert r.status_code == 201
#
#     # 2. Listar usuarios
#     r2 = client.get("/users/")
#     assert any(u["email"] == "ana@example.com" for u in r2.json())

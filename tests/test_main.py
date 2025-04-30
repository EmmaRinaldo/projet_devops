import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

# Livre de test à réutiliser
test_book = {
    "title": "Test Book",
    "author": "Author Test",
    "rating": 4,
    "comment": "A simple comment"
}

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue dans l'API BookReview"}

def test_add_book():
    response = client.post("/books", json=test_book)
    assert response.status_code == 201
    assert response.json() == {"message": "Livre ajouté avec succès"}

def test_list_books():
    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(book["title"] == test_book["title"] for book in data)

def test_get_specific_book():
    response = client.get(f"/books/{test_book['title']}")
    assert response.status_code == 200
    data = response.json()
    assert data["author"] == test_book["author"]

def test_get_nonexistent_book():
    response = client.get("/books/NonExistentTitle")
    assert response.status_code == 404
    assert response.json()["detail"] == "Livre non trouvé"

def test_delete_book():
    response = client.delete(f"/books/{test_book['title']}")
    assert response.status_code == 204

def test_deleted_book_not_found():
    response = client.get(f"/books/{test_book['title']}")
    assert response.status_code == 404

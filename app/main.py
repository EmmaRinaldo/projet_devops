from fastapi import FastAPI, HTTPException
from app.models import Book
from app.database import books

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API BookReview"}

@app.post("/books", status_code=201)
def add_book(book: Book):
    books.append(book)
    return {"message": "Livre ajouté avec succès"}

@app.get("/books")
def list_books():
    return books

@app.get("/books/{title}")
def get_book(title: str):
    for book in books:
        if book.title.lower() == title.lower():
            return book
    raise HTTPException(status_code=404, detail="Livre non trouvé")

@app.delete("/books/{title}", status_code=204)
def delete_book(title: str):
    global books
    books = [b for b in books if b.title.lower() != title.lower()]
    return

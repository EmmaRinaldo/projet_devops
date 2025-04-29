from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    rating: int
    comment: str

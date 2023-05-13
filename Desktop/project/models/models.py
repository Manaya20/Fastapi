from pydantic import BaseModel

class Book(BaseModel):
    book_name: str
    book_author: str
    book_qty: int
    book_id: int
from fastapi import APIRouter, Request,Response

from models.models import Book
from db.database import collection_name

from Schemas.schemas import books_serializer
from Schemas.schemas import book_serializer

from bson import ObjectId

book_api = APIRouter()

# retrieve
@book_api.get("/")
async def get_books():
    books = books_serializer(collection_name.find())
    return books

@book_api.get("get_book/{id}")
async def get_book(book_id: int):
    return books_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# post
@book_api.post("/add_book/")
async def create_book(request: Book):
    data=dict(request)
    _id = collection_name.insert_one(data)
    return books_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@book_api.put("update_book/{id}")
async def update_book(book_id: int, book: Book):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(book)
    })
    return books_serializer(collection_name.find({"_id": ObjectId(id)}))

# delete
@book_api.delete("delete_book/{id}")
async def delete_book(book_id: int):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
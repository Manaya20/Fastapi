
from pymongo import MongoClient



client = MongoClient("mongodb+srv://manayapachpor:Kaustubh285@crudapp.oe8wbhx.mongodb.net/")


db = client.book_app

collection_name = db["books_app"]
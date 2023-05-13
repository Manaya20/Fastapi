
from fastapi import FastAPI
from routes.routes import book_api

app = FastAPI()

app.include_router(book_api)

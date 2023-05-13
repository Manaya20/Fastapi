def book_serializer(Book) -> dict:
    return {
        "book_id": int(Book["_id"]),
        "book_name": Book["name"],
        "book_author": Book["author_name"],
        "book_qty": Book["quantity"],
       
    }

def books_serializer(books) -> dict:
    return [book_serializer(book) for book in books]
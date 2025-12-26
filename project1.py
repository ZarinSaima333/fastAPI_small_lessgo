from fastapi import FastAPI,Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Math"},
    {"title": "Title Two", "author": "Author Two", "category": "Math"},
    {"title": "Title Three", "author": "Author Three", "category": "Computer Science"},
    {"title": "Title Four", "author": "Author Four", "category": "Computer Science"},
    {"title": "Title Five", "author": "Author Five", "category": "Statistics"},
    {"title": "Title Six", "author": "Author Six", "category": "Statistics"},
    {"title": "Title Seven", "author": "Author Seven", "category": "AI"},
    {"title": "Title Eight", "author": "Author Eight", "category": "AI"},
    {"title": "Title Nine", "author": "Author Nine", "category": "Data Science"},
]

@app.get("/books")
async def get_all_books():
    return BOOKS

#path parameter
@app.get('/books/{title}')
async def get_book(title:str):
    for i in BOOKS:
        if i['title'] == title:
            return i
    return {"error": "Book not found"}

#query parameter
@app.get('/books/')
async def get_book_by_category(category:str):
    books_to_return = []
    for i in BOOKS:
        if i['category'] == category:
            books_to_return.append(i)
    return books_to_return

#path and query parameter
@app.get('/books/{book_author}')
async def get_book_by_category(book_author:str, category:str):
    books_to_return = []
    for i in BOOKS:
        if i['author'] == book_author and \
        i['category'] == category:
            books_to_return.append(i)
    return books_to_return

#post request
@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book

#put request
@app.post('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'] == updated_book['title']:
            BOOKS[i] = updated_book
            return BOOKS[i]
    return {"error": "Book not found"}

#delete request
@app.delete('/books/delete_book/{title}')
async def delete_book(title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'] == title:
            BOOKS.pop(i)
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}




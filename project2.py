from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel,Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating


class BookRequest(BaseModel):
    #id:Optional[int]=None
    id:Optional[int]= Field(description="ID is not needed on create",default=None)
    title:str =Field(min_length=3)
    author:str=Field(min_length=1,max_length=15)
    description:str=Field(min_length=1,max_length=100)
    rating:int = Field(gt=0,lt=101)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "shohoj coding shikka",
                "author": "nnj",
                "description": "guchu makes learning easy!",
                "rating": 4      
            }
        }
    }


Books = [
    Book(1,"Let's learn coding","zsr","easy_peasy_lemon_squeezy_codingggg",5),
    Book(2,"shohoj coding shikka","nnj","guchu makes learning easy!",4),
    Book(3,"Shield","Abbu","see life diffferently",3),
    Book(4,"Always there","NAJMD","friends bond get stronger",5),
    Book(5,"Mothers know the best","Ammu","read this book to make moms life easy",4),
    Book(6,"StatFun","roza","easy_peasy_lemon_squeezY_stat",5)
]

@app.get('/books')
async def getBook(status_code=status.HTTP_200_OK):
    return Books
'''
@app.post("/create-book")
async def createBook(new_book=Body()):
    Books.append(new_book) #you've to put the string in a dictionary format
'''
@app.get('/book/')
async def get_book_by_rating(book_rating:int=Query(gt=0,lt=6)):
    get_book_by_rating = []
    for i in Books:
        if i.rating==book_rating:
            get_book_by_rating.append(i)
    return get_book_by_rating

@app.get('/book/{book_id}',status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id:int=Path(gt=0)):
    Book_by_id = []
    for i in Books:
        if i.id==book_id:
            Book_by_id.append(i)
            return Book_by_id

        
    raise HTTPException(status_code=404,detail="id not found")



#Since using Body() I can put whatever i want i need to have some sort of validation. that's why Pydantic!
#What's Pydantic?
#Python library for data modeling,parsing, and has efficient error handling
#So 1.create a differnet request model for validation 2.field data validation for each variable/element

@app.post("/create-book",status_code=status.HTTP_201_CREATED)
async def createBook(book_req : BookRequest):
    #type(book_req)
    new_book=Book(**book_req.model_dump())
    print(type(new_book)) #converting the req to Book object
    new_book = find_book(new_book)   # 🔥 IMPORTANT
    Books.append(new_book)
#We now have a example value schema which we didnt have earlier

# @app.post("/book/update-book")
# async def updated_whole_book(new_book:BookRequest):
#     for i in Books:
#         if i.id==new_book.id:
#             i=new_book

@app.put("/book/update-book",status_code=status.HTTP_204_NO_CONTENT)
async def updated_whole_book(new_book:BookRequest):
    book_change = False
    for i in range(len(Books)):
        if Books[i].id==new_book.id:
            Books[i]=new_book
            book_change=True
    if not book_change:
        raise HTTPException(status_code=404,detail="item not found")


def find_book(book: Book):
    if len(Books)>1:
        book.id = Books[-1].id +1
    else:
        book.id = 1
    return book


@app.delete("/book/(book_id)",status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(book_id:int=Path(gt=0)):
    book_change = False
    for i in range(len(Books)):
        if Books[i].id==book_id:
            Books.pop(i)
            book_change=True
    if not book_change:
        raise HTTPException(status_code=404,detail="item not found")
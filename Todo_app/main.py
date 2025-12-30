#root
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import model
from model import Todo
from database import engine, session_local

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

#after making this file we'll start the uvicorn command and automatically todo.db will be created

def get_db():
    db = session_local()
    try:
        yield db #yield shoho get_db porjonto jabe, er ager part, response pathanor ag porjonto, only uses db when using it, colses after, safe and fast.
    finally:
        db.close() #afyer the response has been deleivered


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todo).all()





#root
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends,HTTPException,status,Path
#import model not needed
from model import Todo
from database import  session_local #removing engine
from pydantic import BaseModel,Field
#from routers import auth not needed

router = APIRouter()

#model.Base.metadata.create_all(bind=engine)

#after making this file we'll start the uvicorn command and automatically todo.db will be created

#router.include_router(auth.router)

def get_db():
    db = session_local()
    try:
        yield db #yield shoho get_db porjonto jabe, er ager part, response pathanor ag porjonto, only uses db when using it, colses after, safe and fast.
    finally:
        db.close() #afyer the response has been deleivered


db_dependency = Annotated[Session, Depends(get_db)]

#pydantic req: it is a todos req of a post http req of a body of a todo, validaton

class TodoReq(BaseModel):
    title:str = Field(min_length=3)
    description:str = Field(min_length=3,max_length=100)
    priority: int= Field(gt=0, lt=6)
    complete:bool

@router.get("/",status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todo).all()


@router.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(db:db_dependency, todo_id:int=Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id== todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail="Todo not found.")

@router.post("/todo",status_code=status.HTTP_200_OK)
async def create_todo(db:db_dependency,todo_req:TodoReq):
    todo_model=Todo(**todo_req.model_dump())
    db.add(todo_model)
    db.commit()


@router.put('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency,
                       todo_req:TodoReq,
                      todo_id:int=Path(gt=0)#error if put before todo_req should be above of anything hat deala with a path paramter
                     ):
    
    todo_model=db.query(Todo).filter(Todo.id==todo_id).first()
    if todo_model is None:
        
        raise HTTPException(status_code=404,detail="Todo not found.")
    todo_model.title = todo_req.title
    todo_model.description = todo_req.description
    todo_model.priority=todo_req.priority
    todo_model.complete=todo_req.complete
    
    
    db.add(todo_model)
    db.commit()

@router.delete("\todo\{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model=db.query(Todo).filter(Todo.id==todo_id).first()
    if todo_model is None:    
        raise HTTPException(status_code=404,detail="Todo not found.")
    db.query(Todo).filter(Todo.id==todo_id).delete()
    db.commit()

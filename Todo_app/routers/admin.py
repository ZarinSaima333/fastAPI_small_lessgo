#root
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends,HTTPException,status,Path
#import model not needed
from model import Todo
from database import  session_local #removing engine
from pydantic import BaseModel,Field
from .auth import get_current_user
#from routers import auth not needed

router = APIRouter(
     prefix="/admin", 
    tags=['admin'])

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
user_dependency = Annotated[dict,Depends(get_current_user)]

@router.get('/todo',status_code=status.HTTP_200_OK)
async def get_all(db:db_dependency,
                  user:user_dependency):
    if user in None or user.get('user_role')!='admin':
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return db.query(Todo).all()
    
@router.delete('/todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    db:db_dependency,
    user:user_dependency,
    todo_id:int=Path(gt=0)
    ):
    if user in None or user.get('user_role')!='admin':
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model=db.query(Todo).filter(Todo.id==todo_id).first()
    if todo_model in None:
        raise HTTPException(status_code=404,detal='todo not found')
    db.query(Todo).filter(Todo.id==todo_id).delete()
    db.commit()
from fastapi import FastAPI, APIRouter, Depends,HTTPException,status,Path
from typing import Annotated
from sqlalchemy.orm import Session
from database import  session_local
from pydantic import BaseModel
from model import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

router =  APIRouter()


bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

class CreateUserReq(BaseModel):
    username: str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str

#get db

def get_db():
    db = session_local()
    try:
        yield db #yield shoho get_db porjonto jabe, er ager part, response pathanor ag porjonto, only uses db when using it, colses after, safe and fast.
    finally:
        db.close() #afyer the response has been deleivered


db_dependency = Annotated[Session, Depends(get_db)]

def autheniocate_user(username:str,password:str,db):
    user= db.query(Users).filter(Users.username==username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_pass):
        return False
    return True #correct pass




@router.post("/auth/",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,create_user_req:CreateUserReq):
    #create_user_model = Users(**create_user_req.model_dump())
    #uporer ta use korbo na karon class create users e password ase, ar amr model,py e ase  hashed_pass= Column(String) basically db er table er column er shathe pydantic naam mile nai.
    create_user_model = Users(
        email=create_user_req.email,
        username=create_user_req.username,
        first_name= create_user_req.first_name,
        last_name= create_user_req.last_name,
        role=create_user_req.role,
        hashed_pass=bcrypt_context.hash(create_user_req.password),
        is_active=True #pydantic class e nai

    )

    db.add(create_user_model) #ekhono post req er output null ashe, sqlite e dekhte pai cmd te,db te save hoise.
    db.commit()
    return create_user_model #correct

    #return {'user': "authentication"} return charao possible, response body te 200 ashe

#wont create two app/port learn about routing:)

#authentication tasks started!

@router.post("/token")
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db:db_dependency):
    user= autheniocate_user(form_data.username,form_data.password,db)
    if not user:
        return "Faslse Authentication"
    return "Succsessful Authentication"


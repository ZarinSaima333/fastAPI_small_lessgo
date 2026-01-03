from fastapi import FastAPI, APIRouter, Depends,HTTPException,status,Path
from typing import Annotated
from sqlalchemy.orm import Session
from database import  session_local
from pydantic import BaseModel
from model import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2AuthorizationCodeBearer,OAuth2PasswordBearer
from jose import jwt,JWTError 
from datetime import timedelta,timezone,datetime


router =  APIRouter(
    prefix="/auth",  #swagger e start hob eita diye endpoint
    tags=['auth']  #swagger e alada vabe dekha jabe
)

SECRET_KEY="69697acb995d927f038f3fe90e96c2aa25107314cfeeeed508a71545274ed4f7"
ALGORITHM='HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


class CreateUserReq(BaseModel):
    username: str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str

class Token(BaseModel):
    access_token:str
    token_type:str

#get db

def get_db():
    db = session_local()
    try:
        yield db #yield shoho get_db porjonto jabe, er ager part, response pathanor ag porjonto, only uses db when using it, colses after, safe and fast.
    finally:
        db.close() #afyer the response has been deleivered


db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(username:str,password:str,db):
    user= db.query(Users).filter(Users.username==username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_pass):
        return False
    #return True #correct pass
    return user

def create_access_token(username:str,user_id:id,role:str,expire_delta:timedelta):
    #create encoding of jwt

    encode={'sub':username,'id':user_id,'role':role}
    expires = datetime.now(timezone.utc)+expire_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

#decode
async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):#dependency injection of oauth bearer
    try:
        payload =jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str= payload.get('sub') #sub holo username
        user_id:int = payload.get('id')
        user_role:str= payload.get('role') #this is recieved by admin.py

        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user')
        return {'username':username,'id':user_id,'user_role':user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user')



@router.post("/",status_code=status.HTTP_201_CREATED)
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

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db:db_dependency):
    user= authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user')
        #return "Faslse Authentication"
    token = create_access_token(user.username,user.id,user.role,timedelta(minutes=20)) #encode
    
    return {'access_token':token,'token_type':'bearer'}
    #return token


#root
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends,HTTPException,status,Path
from ..model import Users
from ..model import Todo
from ..database import  session_local #removing engine
from pydantic import BaseModel,Field
from passlib.context import CryptContext
from .auth import get_current_user
#from routers import auth not needed

router = APIRouter(
     prefix="/user", 
    tags=['user'])



def get_db():
    db = session_local()
    try:
        yield db #yield shoho get_db porjonto jabe, er ager part, response pathanor ag porjonto, only uses db when using it, colses after, safe and fast.
    finally:
        db.close() #afyer the response has been deleivered


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]
#print(user)#{'username': 'zarinsaima', 'id': 3, 'user_role': 'string'}
#print(db) <sqlalchemy.orm.session.Session object at 0x00000212EE411610>
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')


class UserVerification(BaseModel):
    old_pass:str
    new_pass:str=Field(min_length=2) #dif between min_len and gt

@router.get("/",status_code=status.HTTP_200_OK)
async def get_user_info(db:db_dependency,user:user_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    return db.query(Users).filter(Users.id==user.get('id')).first()

'''
returned Response Body:
{
  "first_name": "string",
  "id": 3,
  "email": "zarinsaima",
  "hashed_pass": "$2b$12$KGWujOG7rTQfbcxRnwPUje.PiB.5ALxacA/BEQzkK18clSAOzsBHq",
  "role": "string",
  "last_name": "string",
  "username": "zarinsaima",
  "is_active": true
}
'''
# user_verification:UserVerification expect body and req
@router.put("/password",status_code=status.HTTP_204_NO_CONTENT)
async def pass_change(db:db_dependency,user:user_dependency, user_verification:UserVerification):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")
    user_model= db.query(Users).filter(Users.id==user.get('id')).first() #user_model returs a class obj user returns

    if not bcrypt_context.verify(user_verification.old_pass,user_model.hashed_pass): #massive mistake, user.hashed_pass is expecting a user object but i had a dict. mistake is it should be user_model 
        raise HTTPException(status_code=401,detail="Error on password change")

    user_model.hashed_pass=bcrypt_context.hash(user_verification.new_pass)
    db.add(user_model)
    db.commit()

@router.put("/phonenumber/{new_phone}", status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(
    new_phone: str,
    db: db_dependency,
    user: user_dependency
):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_model.phone_number = new_phone
    db.add(user_model)
    db.commit()
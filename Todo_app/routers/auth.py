from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from model import Users
router =  APIRouter()

class CreateUserReq(BaseModel):
    username: str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str

@router.post("/auth/")
async def create_usuer(create_user_req:CreateUserReq):
    #create_user_model = Users(**create_user_req.model_dump())
    #uporer ta use korbo na karon class create users e password ase, ar amr model,py e ase  hashed_pass= Column(String)
    create_user_model = Users(
        email=create_user_req.email,
        username=create_user_req.username,
        first_name= create_user_req.first_name,
        last_name= create_user_req.last_name,
        role=create_user_req.role,
        hashed_pass=create_user_req.password,
        is_active=True #pydantic class e nai

    )
    return {'user': "authentication"}

#wont create two app/port learn about routing:)
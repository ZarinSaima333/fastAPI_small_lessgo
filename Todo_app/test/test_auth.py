from .utlis import *
from ..routers.auth import get_db,authenticate_user,create_access_token,SECRET_KEY,ALGORITHM,get_current_user
from jose import jwt
from datetime import timedelta,timezone,datetime
import pytest
from fastapi import HTTPException
app.dependency_overrides[get_db]=override_get_db

def test_authenticate_user(test_user):
    db=testing_session_local()
    authenticate_user_var=authenticate_user(test_user.username,'zarinsaima',db)
    assert authenticate_user_var is not None
    assert authenticate_user_var.username==test_user.username

    non_existing_user=authenticate_user("bhuluser","zarinsaima",db)
    assert non_existing_user is False

    wrong_pass_user=authenticate_user(test_user.username,'zarinsaima_bhul',db)
    assert authenticate_user_var is not None #i added
    assert authenticate_user_var.username==test_user.username #i added
    assert non_existing_user is False

def test_create_access_token():
    username='zarinsaima'
    user_id=1
    role='user'
    expire_delta=timedelta(days=1)
    token=create_access_token( username,user_id,role,expire_delta)

    decoded_token=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM],options={'verify_signature':False})
    assert decoded_token['sub']==username
    assert decoded_token['id']==user_id
    assert decoded_token['role']==role

@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {'sub':'zarinsaima','id':1,'role':'admin'}
    token=jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM) #not algorithms
    user= await get_current_user(token=token)
    assert user=={'username':'zarinsaima','id':1,'user_role':'admin'}

@pytest.mark.asyncio
async def  test_get_current_user_missing_payload():
    encode={'role':'user'}
    token=jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token=token)
    
    assert excinfo.value.status_code==401
    assert excinfo.value.detail=='Could not validate user'


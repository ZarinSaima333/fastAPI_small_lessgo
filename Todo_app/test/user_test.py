from ..routers.user import UserVerification
from .utlis import *
from ..routers.user import get_db,get_current_user #router.user I wrote router.admin was returning null json cz quering from another file.
from fastapi import status
from ..model import Todo,Users
from fastapi.testclient import TestClient
from ..main import app


app.dependency_overrides[get_db]=override_get_db
app.dependency_overrides[get_current_user]=override_get_current_user


def test_return_user(test_user): #test_user na dile oitar kichui nibena
    response= client.get('/user/')
    assert response.status_code==status.HTTP_200_OK
    #assert response.json() is None #nothing is returning so we need to create one fixture
    data = response.json()
    assert data["id"] == 1
    assert data["email"] == "zarinsaima"
    assert data["first_name"] == "zarin"
    assert data["last_name"] == "saima"
    assert data["role"] == "admin"
    assert data["phone_number"] == "017123456"



def test_pass_change_success(test_user):
    req_data={'old_pass':"zarinsaima", #pydantic filed match na korle error dibe
              'new_pass':'zarinsaima1'}
    response= client.put('/user/password',json=req_data)
    assert response.status_code==204 #worked finally!!

    # db= testing_session_local()
    # model=db.query(Users).filter(Users.id==1).first()
    # assert model.title=='change the title'


def test_pass_change_unsuccessful(test_user):
    req_data={'old_pass':"wrongpass", #pydantic filed match na korle error dibe
              'new_pass':'zarinsaima1'}
    response= client.put('/user/password',json=req_data)
    assert response.status_code==status.HTTP_401_UNAUTHORIZED #worked finally!!
    assert response.json()=={'detail':"Error on password change"}


def test_phone_number_change(test_user):
    response=client.put('/user/phonenumber/22222222')
    assert response.status_code==status.HTTP_204_NO_CONTENT
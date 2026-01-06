from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker,Session
from ..model import Base 
from fastapi import Depends,status,dependencies
from typing import Annotated
from ..main import app
from ..routers.todo import get_db,get_current_user
from fastapi.testclient import TestClient
import pytest

SQLALCHEMY_DATABASE_URL="sqlite:///./testdb.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={'check_same_thread':False},
                       poolclass = StaticPool
                       )

testing_session_local = sessionmaker(autocommit=False,
                                     autoflush=False,
                                     bind=engine)


Base.metadata.create_all(bind=engine)

def override_get_db():
    db = testing_session_local()
    try:
        yield db #yield shoho get_db porjonto jabe, er ager part, response pathanor ag porjonto, only uses db when using it, colses after, safe and fast.
    finally:
        db.close()

def override_get_current_user():
    return {'username':'zarinsaima',
            'id':1,
            'user_role':'admin'}

app.dependency_overrides[get_db]=override_get_db
app.dependency_overrides[get_current_user]=override_get_current_user

client = TestClient(app)

def test_read_all_authenticated():
    response = client.get('/')
    assert response.status_code==status.HTTP_200_OK
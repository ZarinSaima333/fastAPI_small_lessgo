#reusable components will be moved
from ..model import Base, Todo
from sqlalchemy import create_engine,text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker,Session
from ..model import Base, Todo,Users
from ..main import app
import pytest
from fastapi.testclient import TestClient
from ..routers.user import bcrypt_context


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
            'user_role':'admin'} #chaning admin to non admin because 
client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todo(
        title= "Learn to code",
        description="Need to learn everything",
        priority=5,
        complete=False,
        owner_id=1
    )

    db = testing_session_local()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

@pytest.fixture
def test_user():
    users_mock = Users(
        id =1,
        email="zarinsaima",
        username="zarinsaima",
        first_name='zarin',
        last_name='saima',
        hashed_pass=bcrypt_context.hash("zarinsaima"),
        role='admin',
        phone_number='017123456'

    )

    db = testing_session_local()
    db.add(users_mock) #class
    db.commit()
    yield users_mock
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;")) #tavle
        connection.commit()

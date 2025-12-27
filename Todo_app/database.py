from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread" : False}) #fastapi works with multiple thread. Allows FastAPI (multi-threaded) to use the same SQLite connection safely

session_local = sessionmaker(bind=engine,autoflush=False,auto_commit=False) #cause I want  to take the full control of the system autoflush=False → Changes are not sent to DB automatically autocommit=False → You must manually commit

Base = declarative_base() #Every table model will inherit from Base



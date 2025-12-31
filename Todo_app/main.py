#root

from fastapi import FastAPI
import model

from database import engine

from routers import auth, todo

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

#after making this file we'll start the uvicorn command and automatically todo.db will be created

app.include_router(auth.router)
app.include_router(todo.router)

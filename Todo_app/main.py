#root

from fastapi import FastAPI
import model

from database import engine

from routers import auth, todo, admin, user

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

#after making this file we'll start the uvicorn command and automatically todo.db will be created

@app.get("/healthy")
def health_check():
    return{'status':'Healthy'}
app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(admin.router)
app.include_router(user.router)
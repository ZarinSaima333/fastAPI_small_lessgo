from fastapi import FastAPI, APIRouter
router =  APIRouter()

@router.get("/auth/")
async def get_usuer():
    return {'user': "authentication"}

#wont create two app/port learn about routing:)
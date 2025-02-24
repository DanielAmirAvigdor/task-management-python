from fastapi import APIRouter

users_router = APIRouter()


@users_router.get("/")
async def get_user():
    return {"some_user_id": "234"}

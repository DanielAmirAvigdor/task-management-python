from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import CreateUserRequest, CreateUserResponse
from logic import users as users_logic
from data.db import get_db

users_router = APIRouter()


@users_router.get("/{id}")
async def get_user(id: int):
    return {"user_id": id}


@users_router.post("", response_model=CreateUserResponse)
async def create_user(user: CreateUserRequest, db: Session = Depends(get_db)):
    response = users_logic.create_user(user, db)

    return response

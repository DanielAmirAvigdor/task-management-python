from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.users import CreateUserRequest, UserResponse, UpdateUserRequest
from logic import users as users_logic
from data.db import get_db

users_router = APIRouter()


@users_router.get("/{id}")
async def get_user(id: int, db: Session = Depends(get_db)):
    response = users_logic.get_user(id, db)
    return response


@users_router.post("", response_model=UserResponse)
async def create_user(user: CreateUserRequest, db: Session = Depends(get_db)):
    response = users_logic.create_user(user, db)
    return response


@users_router.put("/{id}", response_model=UserResponse)
async def update_user(id: int, user: UpdateUserRequest, db: Session = Depends(get_db)):
    response = users_logic.update_user(user, db)
    return response


@users_router.delete("{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, db: Session = Depends(get_db)):
    success = users_logic.delete_user(id, db)
    return

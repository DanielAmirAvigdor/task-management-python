from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.users import UserResponse, UpdateUserRequest
from logic import users as users_logic
from models.models import User
from auth.dependencies import get_current_user
from data.db import get_db

users_router = APIRouter(tags=["Users"])


@users_router.get("/me", response_model=UserResponse)
async def get_current_user(
    current_user: User = Depends(get_current_user)
):
    return users_logic.get_current_user(current_user)


@users_router.put("/me", response_model=UserResponse)
async def update_user(
    updated_user: UpdateUserRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return users_logic.update_user(current_user.user_id, updated_user, db)


@users_router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    users_logic.delete_user(current_user.user_id, db)

# todo: add /users/me/projects (get all projects for a user)
# todo: add /users/me/tasks (get all tasks for a user)

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas.users import UserResponse, UpdateUserRequest
from logic import users as users_logic
from models.models import User
from auth.dependencies import get_current_user
from data.db import get_db

users_router = APIRouter()


@users_router.get("/{id}", response_model=UserResponse)
async def get_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    return users_logic.get_user(id, db)


@users_router.put("/{id}", response_model=UserResponse)
async def update_user(
    id: int,
    user: UpdateUserRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    return users_logic.update_user(id, user, db)


@users_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    users_logic.delete_user(id, db)

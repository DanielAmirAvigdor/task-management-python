from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.models import User
from backend.app.auth.hashing import hash_password
from data import users as users_data
from schemas.users import UpdateUserRequest



def get_currernt_user(current_user: User) -> User:
    return current_user


def update_user(target_user_id: int, user: UpdateUserRequest, requesting_user_id: int, db: Session) -> User:
    if requesting_user_id != target_user_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    hashed_password = hash_password(user.password) if user.password else None
    return users_data.update_user(target_user_id, user, hashed_password, db)


def delete_user(target_user_id: int, requesting_user_id: int, db: Session) -> bool:
    if requesting_user_id != target_user_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    return users_data.delete_user(target_user_id, db)

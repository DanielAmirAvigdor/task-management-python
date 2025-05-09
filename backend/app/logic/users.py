from sqlalchemy.orm import Session
from models.models import User
from auth.hashing import hash_password
from data import users as users_data
from schemas.users import UpdateUserRequest


def get_current_user(current_user: User) -> User:
    return current_user


def update_user(user_id: int, updated_user: UpdateUserRequest, db: Session) -> User:
    hashed_password = hash_password(updated_user.password) if updated_user.password else None
    return users_data.update_user(user_id, updated_user, hashed_password, db)


def delete_user(user_id: int, db: Session) -> bool:
    return users_data.delete_user(user_id, db)

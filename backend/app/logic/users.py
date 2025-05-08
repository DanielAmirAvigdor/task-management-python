from sqlalchemy.orm import Session
from models.models import User
from auth.hash import hash_password
from data import users as users_data
from schemas.users import CreateUserRequest, UpdateUserRequest


def get_user(id: int, db: Session) -> User:
    user = users_data.get_user(id, db)
    return user


def update_user(id: int, user: UpdateUserRequest, db: Session) -> User:
    hashed_password = None
    if user.password:
        hashed_password = hash_password(user.password)
    return users_data.update_user(id, user, hashed_password, db)


def delete_user(id: int, db: Session) -> bool:
    return users_data.delete_user(id, db)

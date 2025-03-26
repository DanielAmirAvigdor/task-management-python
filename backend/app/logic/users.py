from sqlalchemy.orm import Session
from models.models import User
from utils.hash import hash_password
from data import users as users_data
from schemas.users import CreateUserRequest, UpdateUserRequest


def create_user(user: CreateUserRequest, db: Session) -> User:
    hashed_password = hash_password(user.password)
    user = users_data.create_user(user, hashed_password, db)
    return user


def get_user(id: int, db: Session) -> User:
    user = users_data.get_user(id, db)
    return user


def update_user(id: int, user: UpdateUserRequest, db: Session) -> User:
    hashed_password = hash_password(user.password)
    user = users_data.update_user(id, user, hashed_password, db)
    return user


def delete_user(id: int, db: Session) -> bool:
    return users_data.delete_user(id, db)

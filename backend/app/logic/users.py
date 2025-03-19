from sqlalchemy.orm import Session
from models.models import User
from utils.hash import hash_password
from data import users as users_data
from schemas.users import CreateUserRequest


def create_user(user: CreateUserRequest, db: Session) -> User:
    hashed_password = hash_password(user.password)
    user = users_data.create_user(user, hashed_password, db)
    return user

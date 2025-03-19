from sqlalchemy.orm import Session
from models.models import User
from schemas.users import CreateUserRequest


def create_user(user: CreateUserRequest, hashed_password: str, db: Session) -> User:
    db_user = User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        password_hash=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

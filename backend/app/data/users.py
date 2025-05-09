from typing import Optional
from sqlalchemy.orm import Session
from models.models import User
from schemas.users import UpdateUserRequest


def update_user(user_id: int, user: UpdateUserRequest, hashed_password: Optional[str], db: Session) -> Optional[User]:
    db_user = db.query(User).filter(User.user_id == user_id).first()

    if not db_user:
        return None

    if user.email is not None:
        db_user.email = user.email
    if user.first_name is not None:
        db_user.first_name = user.first_name
    if user.last_name is not None:
        db_user.last_name = user.last_name
    if hashed_password:
        db_user.password_hash = hashed_password

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(user_id: int, db: Session) -> bool:
    db_user = db.query(User).filter(User.user_id == user_id).first()

    if not db_user:
        return False

    db.delete(db_user)
    db.commit()

    return True

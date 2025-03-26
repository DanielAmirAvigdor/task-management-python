from sqlalchemy.orm import Session
from models.models import User
from schemas.users import CreateUserRequest, UpdateUserRequest


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


def get_user(id: int, db: Session) -> User | None:
    return db.query(User).filter(User.id == id).first()


def update_user(id: int, user: UpdateUserRequest, db: Session) -> User | None:
    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        return None

    if user.email is not None:
        db_user.email = user.email
    if user.first_name is not None:
        db_user.first_name = user.first_name
    if user.last_name is not None:
        db_user.last_name = user.last_name

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(id: int, db: Session) -> bool:
    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        return False

    db.delete(db_user)
    db.commit()
    return True

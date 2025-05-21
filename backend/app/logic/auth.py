from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from data import auth as auth_data
from auth.hashing import verify_password, hash_password
from auth.jwt import create_access_token
from schemas.auth import AuthResponse
from schemas.users import CreateUserRequest, UserResponse


def login(email: str, password: str, db: Session) -> AuthResponse:
    user = auth_data.get_user_by_email(email, db)

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    access_token = create_access_token({"sub": str(user.user_id)})

    return AuthResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.model_validate(user)
    )


def register(user: CreateUserRequest, db: Session) -> AuthResponse:
    if auth_data.get_user_by_email(user.email, db):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    user = auth_data.create_user(user, hashed_password, db)

    access_token = create_access_token({"sub": str(user.user_id)})

    return AuthResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.model_validate(user)
    )

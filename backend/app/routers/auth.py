from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from data.db import get_db
from schemas.users import CreateUserRequest
from logic import auth as auth_logic

auth_router = APIRouter(tags=["Auth"])


@auth_router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    username, password = form_data.username, form_data.password
    return auth_logic.login(username, password, db)


@auth_router.post("/register")
def register(
    user: CreateUserRequest,
    db: Session = Depends(get_db)
):
    return auth_logic.register(user, db)

# todo: add refresh token
# todo: add invalidate token

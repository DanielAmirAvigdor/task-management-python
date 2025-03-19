import re
from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime


class CreateUserRequest(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str = Field(min_length=8)
    creation_date: datetime = datetime.now()

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        if not re.match(pattern, value):
            raise ValueError("Password must contain at least 8 characters, including letters and numbers.")
        return value


class CreateUserResponse(BaseModel):
    user_id: int
    email: EmailStr
    first_name: str
    last_name: str
    creation_date: datetime

    class Config:
        orm_mode = True

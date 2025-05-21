import re
from pydantic import BaseModel, EmailStr, ConfigDict, Field, field_validator
from typing import Optional
from datetime import datetime


class UserValidator(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None

    @field_validator("first_name", "last_name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty or just whitespace.")
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        if not re.match(pattern, value):
            raise ValueError("Password must contain at least 8 characters, including letters and numbers.")
        return value


class CreateUserRequest(UserValidator):
    email: EmailStr
    password: str = Field(min_length=8)
    first_name: str
    last_name: str


class UpdateUserRequest(UserValidator):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None


class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
    first_name: str
    last_name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel
from schemas.users import UserResponse


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

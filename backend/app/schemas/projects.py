from typing import Optional
from pydantic import BaseModel, field_validator
from datetime import datetime
from schemas.tasks import TaskResponse
from schemas.users import UserResponse


class ProjectValidator(BaseModel):
    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError("Title can't be empty.")
        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value):
        if value is None:
            return value
        return value.strip()


class CreateProjectRequest(ProjectValidator):
    title: str
    description: Optional[str] = None


class UpdateProjectRequest(ProjectValidator):
    title: Optional[str] = None
    description: Optional[str] = None


class ProjectResponse(BaseModel):
    project_id: int
    title: str
    description: Optional[str] = None
    participants: list[UserResponse]
    tasks: list[TaskResponse]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

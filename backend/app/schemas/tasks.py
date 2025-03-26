from typing import Optional
from pydantic import BaseModel, field_validator
from datetime import datetime
from models.enums import PriorityEnum


class TaskValidatorMixin(BaseModel):
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

    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls, value):
        if value is not None and value < datetime.now():
            raise ValueError("Due date cannot be in the past.")
        return value


class CreateTaskRequest(TaskValidatorMixin):
    project_id: Optional[int] = None
    user_id: int
    title: str
    description: Optional[str] = None
    is_completed: bool
    priority: PriorityEnum = PriorityEnum.LOW
    due_date: Optional[datetime] = None


class UpdateTaskRequest(TaskValidatorMixin):
    project_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = PriorityEnum.LOW
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    task_id: int
    project_id: Optional[int]
    user_id: int
    title: str
    description: Optional[str] = None
    is_completed: bool
    priority: Optional[PriorityEnum] = PriorityEnum.LOW
    due_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

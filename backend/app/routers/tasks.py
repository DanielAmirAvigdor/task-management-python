from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.tasks import TaskResponse, CreateTaskRequest, UpdateTaskRequest
from logic import tasks as tasks_logic
from data.db import get_db
from models.models import User
from auth.dependencies import get_current_user

tasks_router = APIRouter()


@tasks_router.get("/", response_model=List[TaskResponse])
async def get_tasks_by_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return tasks_logic.get_tasks_by_user(current_user.user_id, db)


@tasks_router.get("/{id}", response_model=TaskResponse)
async def get_task(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return tasks_logic.get_task(id, current_user.user_id, db)


@tasks_router.post("", response_model=TaskResponse)
async def create_task(
    task: CreateTaskRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return tasks_logic.create_task(task, current_user.user_id, db)


@tasks_router.put("/{id}", response_model=TaskResponse)
async def update_task(
    id: int,
    task: UpdateTaskRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return tasks_logic.update_task(id, task, current_user.user_id, db)


@tasks_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    tasks_logic.delete_task(id, current_user.user_id, db)

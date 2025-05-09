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
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return tasks_logic.get_tasks_by_user(current_user.user_id, db)


@tasks_router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return tasks_logic.get_task(task_id, current_user.user_id, db)


@tasks_router.post("", response_model=TaskResponse)
async def create_task(
    task: CreateTaskRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return tasks_logic.create_task(task, current_user.user_id, db)


@tasks_router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    updated_task: UpdateTaskRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return tasks_logic.update_task(task_id, updated_task, current_user.user_id, db)


@tasks_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    tasks_logic.delete_task(task_id, current_user.user_id, db)

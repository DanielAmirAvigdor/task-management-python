from fastapi import HTTPException
from typing import List
from sqlalchemy.orm import Session
from models.models import Task
from data import tasks as tasks_data
from utils import permissions
from schemas.tasks import CreateTaskRequest, UpdateTaskRequest


def get_task(task_id: int, user_id: int, db: Session) -> Task:
    task = tasks_data.get_task(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.user_id != user_id:
        if not permissions.is_user_participant(user_id, task.project_id, db):
            raise HTTPException(status_code=403, detail="Unauthorized")

    return task


def create_task(task_data: CreateTaskRequest, user_id: int, db: Session) -> Task:
    return tasks_data.create_task(task_data, user_id, db)


def update_task(task_id: int, updated_task: UpdateTaskRequest, user_id: int, db: Session) -> Task:
    task = tasks_data.get_task(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.user_id != user_id:
        if not permissions.is_user_admin(user_id, task.project_id, db):
            raise HTTPException(status_code=403, detail="Unauthorized")

    return tasks_data.update_task(task_id, updated_task, db)


def delete_task(task_id: int, user_id: int, db: Session) -> bool:
    task = tasks_data.get_task(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.user_id != user_id:
        if not permissions.is_user_admin(user_id, task.project_id, db):
            raise HTTPException(status_code=403, detail="Unauthorized")

    return tasks_data.delete_task(task_id, db)


def get_tasks_by_user_id(user_id: int, db: Session) -> List[Task]:
    tasks = tasks_data.get_tasks_by_user_id(user_id, db)
    return tasks


def get_tasks_by_project_id(user_id: int, project_id: int, db: Session) -> List[Task]:
    tasks = tasks_data.get_tasks_by_project_id(project_id, db)
    return tasks

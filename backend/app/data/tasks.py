from typing import Optional
from sqlalchemy.orm import Session
from models.models import Task
from schemas.tasks import CreateTaskRequest, UpdateTaskRequest


def get_task(task_id: int, db: Session) -> Optional[Task]:
    return db.query(Task).filter(Task.task_id == task_id).first()


def create_task(task: CreateTaskRequest, user_id: int, db: Session) -> Task:
    db_task = Task(
        project_id=task.project_id,
        user_id=user_id,
        title=task.title,
        description=task.description,
        is_completed=task.is_completed,
        priority=task.priority,
        due_date=task.due_date
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def update_task(task_id: int, updated_task: UpdateTaskRequest, db: Session) -> Optional[Task]:
    db_task = db.query(Task).filter(Task.task_id == task_id).first()
    if not db_task:
        return None

    if updated_task.project_id is not None:
        db_task.project_id = updated_task.project_id
    if updated_task.title is not None:
        db_task.title = updated_task.title
    if updated_task.description is not None:
        db_task.description = updated_task.description
    if updated_task.is_completed is not None:
        db_task.is_completed = updated_task.is_completed
    if updated_task.priority is not None:
        db_task.priority = updated_task.priority
    if updated_task.due_date is not None:
        db_task.due_date = updated_task.due_date

    db.commit()
    db.refresh(db_task)

    return db_task


def delete_task(task_id: int, db: Session) -> bool:
    db_task = db.query(Task).filter(Task.task_id == task_id).first()
    if not db_task:
        return False

    db.delete(db_task)
    db.commit()

    return True


def get_tasks_by_user_id(user_id: int, db: Session) -> list[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()


def get_tasks_by_project_id(project_id: int, db: Session) -> list[Task]:
    return db.query(Task).filter(Task.project_id == project_id).all()

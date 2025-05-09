from sqlalchemy.orm import Session
from models.models import Task
from schemas.tasks import CreateTaskRequest, UpdateTaskRequest


def get_tasks_by_user(user_id: int, db: Session) -> list[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()


def get_task(id: int, db: Session) -> Task | None:
    return db.query(Task).filter(Task.id == id).first()


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


def update_task(id: int, task: UpdateTaskRequest, db: Session) -> Task | None:
    db_task = db.query(Task).filter(Task.id == id).first()
    if not db_task:
        return None

    if task.project_id is not None:
        db_task.project_id = task.project_id
    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.is_completed is not None:
        db_task.is_completed = task.is_completed
    if task.priority is not None:
        db_task.priority = task.priority
    if task.due_date is not None:
        db_task.due_date = task.due_date

    db.commit()
    db.refresh(db_task)

    return db_task


def delete_task(id: int, db: Session) -> bool:
    db_task = db.query(Task).filter(Task.id == id).first()
    if not db_task:
        return False

    db.delete(db_task)
    db.commit()

    return True

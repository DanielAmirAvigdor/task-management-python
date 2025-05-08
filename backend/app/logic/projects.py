from fastapi import HTTPException
from typing import List
from sqlalchemy.orm import Session
from models.models import Project
from data import projects as projects_data


def get_projects_by_user(user_id: str, db: Session) -> List[Project]:
    projects = projects_data.get_projects_by_user(user_id, db)
    return projects


def get_project(id: int, user_id: int, db: Session) -> Project:
    project = projects_data.get_project(id, user_id, db)
    if not project or project.user_id != user_id
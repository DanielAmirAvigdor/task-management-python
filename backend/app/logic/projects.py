from fastapi import HTTPException
from typing import List
from sqlalchemy.orm import Session
from models.models import Project
from schemas.projects import CreateProjectRequest, UpdateProjectRequest
from data import projects as projects_data
from utils import permissions


def get_projects_by_user(user_id: str, db: Session) -> List[Project]:
    projects = projects_data.get_projects_by_user(user_id, db)
    return projects


def get_project(project_id: int, user_id: int, db: Session) -> Project:
    if not permissions.is_user_participant(user_id, project_id, db):
        raise HTTPException(status_code=403, detail="Unathorized")

    project = projects_data.get_project(project_id, db)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


def create_project(project: CreateProjectRequest, user_id: int, db: Session) -> Project:
    return projects_data.create_project(project, user_id, db)


def update_project(project_id: int, project: UpdateProjectRequest, db: Session, user_id: int) -> Project:
    project = projects_data.get_project(project_id, db)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if not permissions.is_user_admin(user_id, project_id, db):
        raise HTTPException(status_code=403, detail="Unathorized")

    return projects_data.update_project(project_id, project, db)


def delete_project(project_id: int, user_id: int, db: Session) -> bool:
    project = projects_data.get_project(project_id, db)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not permissions.is_user_admin(user_id, project_id, db):
        raise HTTPException(status_code=403, detail="Unathorized")

    return projects_data.delete_project(project_id, db)

from typing import List
from data.db import get_db
from logic import projects as projects_logic
from fastapi import APIRouter, Depends, status
from auth.dependencies import get_current_user
from sqlalchemy.orm import Session
from models.models import User
from schemas.projects import ProjectResponse, CreateProjectRequest, UpdateProjectRequest

projects_router = APIRouter()


@projects_router.get("/", response_model=List[ProjectResponse])
async def get_projects_by_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return projects_logic.get_projects_by_user(current_user.user_id, db)


@projects_router.get("/{id}", response_model=ProjectResponse)
async def get_project(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return projects_logic.get_project(id, current_user.user_id, db)


@projects_router.post("/", response_model=ProjectResponse)
async def create_project(
    project: CreateProjectRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return projects_logic.create_project(project, current_user.user_id, db)


@projects_router.put("/{id}", response_model=ProjectResponse)
async def update_project(
    id: int,
    project: UpdateProjectRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return projects_logic.update_project(id, project, current_user.user_id, db)


@projects_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    projects_logic.delete_project(id, current_user.user_id, db)

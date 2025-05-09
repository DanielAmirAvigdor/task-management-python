from typing import List
from data.db import get_db
from logic import projects as projects_logic
from fastapi import APIRouter, Depends, status
from auth.dependencies import get_current_user
from sqlalchemy.orm import Session
from models.models import User
from schemas.projects import ProjectResponse, CreateProjectRequest, UpdateProjectRequest

projects_router = APIRouter(tags=["Projects"])

# todo: remove this function (redundant for /users/me/projects)
@projects_router.get("/", response_model=List[ProjectResponse])
async def get_projects_by_user(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return projects_logic.get_projects_by_user(current_user.user_id, db)


@projects_router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return projects_logic.get_project(project_id, current_user.user_id, db)


@projects_router.post("/", response_model=ProjectResponse)
async def create_project(
    project: CreateProjectRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return projects_logic.create_project(project, current_user.user_id, db)


@projects_router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: int,
    project: UpdateProjectRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return projects_logic.update_project(project_id, project, current_user.user_id, db)


@projects_router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    projects_logic.delete_project(project_id, current_user.user_id, db)


# todo: add /projects/project_id/tasks - get all tasks for project

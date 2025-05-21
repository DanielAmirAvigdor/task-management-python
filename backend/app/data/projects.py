from typing import Optional
from sqlalchemy.orm import Session
from models.models import Project, UserProject
from schemas.projects import CreateProjectRequest, UpdateProjectRequest


def get_project(project_id: int, db: Session) -> Optional[Project]:
    return db.query(Project).filter(Project.project_id == project_id).first()


def create_project(project: CreateProjectRequest, user_id: int, db: Session) -> Project:
    db_project = Project(
        title=project.title,
        description=project.description
    )
    db.add(project)
    db.commit()
    db.refresh(project)

    link = UserProject(
        user_id=user_id,
        project_id=db_project.project_id,
        is_admin=True
    )
    db.add(link)
    db.commit()

    return db_project


def update_project(project_id: int, updated_project: UpdateProjectRequest, db: Session) -> Project:
    project = db.query(Project).filter(Project.project_id == project_id).first()

    if updated_project.title is not None:
        project.title = updated_project.title
    if updated_project.description is not None:
        project.description = updated_project.description

    db.commit()
    db.refresh(project)

    return project


def delete_project(project_id: int, db: Session) -> bool:
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        return False

    db.delete(project)
    db.commit()

    return True


def get_projects_by_user_id(user_id: int, db: Session) -> list[Project]:
    return (
        db.query(Project)
        .join(UserProject, UserProject.project_id == Project.project_id)
        .filter(UserProject.user_id == user_id)
        .all()
    )

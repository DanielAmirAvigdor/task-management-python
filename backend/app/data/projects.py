from sqlalchemy.orm import Session
from models.models import Project, UserProject
from schemas.projects import CreateProjectRequest, UpdateProjectRequest


def get_projects_by_user(user_id: int, db: Session) -> list[Project]:
    return (
        db.query(Project)
        .join(UserProject, UserProject.project_id == Project.project_id)
        .filter(UserProject.user_id == user_id)
        .all()
    )


def get_project(project_id: int, db: Session) -> Project | None:
    return db.query(Project).filter(Project.project_id == project_id).first()


def create_project(project_data: CreateProjectRequest, user_id: int, db: Session) -> Project:
    project = Project(
        title=project_data.title,
        description=project_data.description
    )
    db.add(project)
    db.commit()
    db.refresh(project)

    link = UserProject(
        user_id=user_id,
        project_id=project.project_id,
        is_admin=True
    )
    db.add(link)
    db.commit()

    return project


def update_project(project_id: int, data: UpdateProjectRequest, db: Session) -> Project:
    project = db.query(Project).filter(Project.project_id == project_id).first()

    if data.title is not None:
        project.name = data.title
    if data.description is not None:
        project.description = data.description

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

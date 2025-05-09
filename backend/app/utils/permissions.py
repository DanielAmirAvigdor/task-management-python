from sqlalchemy.orm import Session
from models.models import UserProject


def is_user_participant(user_id: int, project_id: int, db: Session) -> bool:
    return (
        db.query(UserProject)
        .filter(
            UserProject.user_id == user_id,
            UserProject.project_id == project_id
        )
        .first()
        is not None
    )


def is_user_admin(user_id: int, project_id: int, db: Session) -> bool:
    link = (
        db.query(UserProject)
        .filter(
            UserProject.user_id == user_id,
            UserProject.project_id == project_id
        )
        .first()
    )
    return link is not None and link.is_admin

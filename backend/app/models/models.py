from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enums import RoleEnum, PriorityEnum
from db import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    tasks = relationship("Task", back_populates="user")
    projects = relationship("UserProject", back_populates="user")


class Project(Base):
    __tablename__ = "projects"
    project_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    tasks = relationship("Task", back_populates="project")
    users = relationship("UserProject", back_populates="project")


class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Boolean, default=False, nullable=False)
    priority = Column(Enum(PriorityEnum), nullable=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship("User", back_populates="tasks")
    project = relationship("Project", back_populates="tasks")


class UserProject(Base):
    __tablename__ = "user_projects"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), primary_key=True)
    role = Column(Enum(RoleEnum), nullable=False)

    user = relationship('User', back_populates='projects')
    project = relationship('Project', back_populates='users')

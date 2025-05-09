from fastapi import FastAPI
from routers.users import users_router
from routers.tasks import tasks_router
from routers.projects import projects_router
from routers.auth import auth_router

app = FastAPI()

app.include_router(users_router, prefix="/users")
app.include_router(tasks_router, prefix="/tasks")
app.include_router(projects_router, prefix="/projects")
app.include_router(auth_router, prefix="/auth")

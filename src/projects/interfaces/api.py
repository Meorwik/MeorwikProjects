from fastapi import APIRouter

from projects.interfaces.routes import projects_router, users_router

api_router = APIRouter()
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(projects_router, prefix="/projects", tags=["projects"])

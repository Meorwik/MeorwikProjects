from src.domain.entities.project import Project, ProjectPhoto
from .schemas.project import ProjectCreate
from src.domain.project_manager import StdOut, StdIn
from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()


@router.get("/")
@inject
def get_projects(gateway: FromDishka[StdOut]) -> List[Project]:
    projects = gateway.get_projects()
    return projects


@router.get("/{project_id}")
@inject
def get_project(project_id: int, gateway: FromDishka[StdOut]) -> Project:
    project = gateway.get_project(project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.post("/")
@inject
def create_project(project_create: ProjectCreate, gateway: FromDishka[StdIn]) -> Project:
    domain_project = Project(
        name=project_create.name,
        description=project_create.description,
        media=[ProjectPhoto(photo=media.photo) for media in project_create.media]
    )
    project: Project = gateway.add_project(domain_project)
    return project
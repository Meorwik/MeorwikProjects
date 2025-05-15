from typing import List

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException

from projects.domain.entities.project import Project, ProjectPhoto
from projects.domain.project_manager import StdIn, StdOut

from .schemas.project import ProjectCreate

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
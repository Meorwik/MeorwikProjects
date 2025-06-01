from typing import List

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException

from projects.domain.entities import Project, ProjectPhoto
from projects.domain.protocols import ProjectGateway
from projects.interfaces.schemas import ProjectCreate

projects_router = APIRouter()


@projects_router.get("/")
@inject
def get_projects(gateway: FromDishka[ProjectGateway]) -> List[Project]:
    projects: List[Project] = gateway.get_projects()
    return projects


@projects_router.get("/{project_id}")
@inject
def get_project(project_id: int, gateway: FromDishka[ProjectGateway]) -> Project:
    project = gateway.get_project(project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@projects_router.post("/")
@inject
def create_project(
    project_create: ProjectCreate, gateway: FromDishka[ProjectGateway]
) -> Project:
    domain_project = Project(
        name=project_create.name,
        description=project_create.description,
        media=[ProjectPhoto(photo=media.photo) for media in project_create.media],
    )
    project: Project = gateway.add_project(domain_project)
    return project

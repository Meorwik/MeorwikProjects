from domain.entities.project import Project, ProjectPhoto
from schemas.project import ProjectCreate, ProjectResponse
from db.storage_manager import FSStorageGateway
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter(prefix="/projects", tags=["Projects"])




@router.get("/", response_model=List[ProjectResponse])
def get_projects():
    projects = gateway.get_projects()
    return projects


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int):
    project = gateway.get_project(project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.post("/", response_model=ProjectResponse)
def create_project(project_create: ProjectCreate):
    domain_project = Project(
        id=0,
        name=project_create.name,
        description=project_create.description,
        media=[ProjectPhoto(photo=media.photo) for media in project_create.media]
    )
    project: Project = gateway.add_project(domain_project)
    return ProjectResponse(id=project.id, name=project.name, description=project.description, media=project.media)
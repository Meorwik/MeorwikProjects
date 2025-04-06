from domain.entities.project import Project, ProjectPhoto
from domain.project_manager import ProjectsGateway
from db.storage_manager import FSStorageGateway
from interfaces.routes import *
from fastapi import FastAPI
from typing import Final, List


def start_app():
    fastapi_app: Final[FastAPI] = FastAPI()
    


if __name__ == '__main__':
    start_app()
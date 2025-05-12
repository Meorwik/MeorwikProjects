from typing import Final

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.domain.dependencies import ProjectGateProvider
from src.interfaces.routes import router

app: Final[FastAPI] = FastAPI()
app.include_router(router, tags=["Projects"], prefix="/projects")
container = make_async_container(ProjectGateProvider(), context={})
setup_dishka(container, app)


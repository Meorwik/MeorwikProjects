from typing import Final

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from projects.domain.dependencies import ProjectGateProvider, UserGateProvider
from projects.interfaces.api import api_router

app: Final[FastAPI] = FastAPI()
app.include_router(api_router, prefix="/api")
container = make_async_container(UserGateProvider(), ProjectGateProvider(), context={})
setup_dishka(container, app)

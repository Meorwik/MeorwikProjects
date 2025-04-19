from src.domain.dependencies import ProjectGateProvider
from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container
from src.interfaces.routes import router
from fastapi import FastAPI
from typing import Final

app: Final[FastAPI] = FastAPI()
app.include_router(router, tags=["Projects"], prefix="/projects")
container = make_async_container(ProjectGateProvider(), context={})
setup_dishka(container, app)

def start_app():
    ...


if __name__ == '__main__':
    start_app()
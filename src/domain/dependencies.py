from .project_manager import StdOut, StdIn, ProjectGateway
from dishka import Provider, Scope, provide, AnyOf
from src.db.storage_manager import FSStorageGateway


class ProjectGateProvider(Provider):
    get_project_gate = provide(
        FSStorageGateway,
        provides=AnyOf[StdIn, StdOut, ProjectGateway],
        scope=Scope.REQUEST,
    )


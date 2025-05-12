from dishka import AnyOf, Provider, Scope, provide

from src.db.storage_manager import FSStorageGateway

from .project_manager import ProjectGateway, StdIn, StdOut


class ProjectGateProvider(Provider):
    get_project_gate = provide(
        FSStorageGateway,
        provides=AnyOf[StdIn, StdOut, ProjectGateway],
        scope=Scope.REQUEST,
    )


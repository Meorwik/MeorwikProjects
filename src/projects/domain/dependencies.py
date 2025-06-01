from dishka import AnyOf, Provider, Scope, provide

from projects.db import FSProjectsGateway, FSUserGateway
from projects.domain import ProjectGateway, UsersGateway


class ProjectGateProvider(Provider):
    get_project_gate = provide(
        FSProjectsGateway,
        provides=AnyOf[ProjectGateway],
        scope=Scope.REQUEST,
    )


class UserGateProvider(Provider):
    get_user_gate = provide(
        FSUserGateway,
        provides=AnyOf[UsersGateway],
        scope=Scope.REQUEST,
    )

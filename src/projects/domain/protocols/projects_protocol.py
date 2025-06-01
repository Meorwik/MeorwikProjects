from typing import List, Protocol

from projects.domain.entities.project import Project


class ProjectGateway(Protocol):

    def get_project(self, project_id: int) -> Project: ...

    def get_projects(self) -> List[Project]: ...

    def add_projects(self, project: Project) -> List[Project]: ...

    def add_project(self, project: Project) -> Project: ...

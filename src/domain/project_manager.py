from src.domain.entities.project import Project
from typing import List, Protocol


class StdIn(Protocol):
    def add_projects(self, project: Project) -> List[Project]: ...

    def add_project(self, project: Project) -> Project: ...


class StdOut(Protocol):
    def get_project(self, project_id: int) -> Project: ...

    def get_projects(self) -> List[Project]: ...


class ProjectGateway(StdIn, StdOut):
    ...
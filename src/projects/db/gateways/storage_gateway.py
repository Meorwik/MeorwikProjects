import json
from dataclasses import asdict
from typing import Any, Dict, List

from projects.db.gateways.base import FSStorageGateway

from projects.domain import ProjectGateway
from projects.domain.entities import Project, ProjectPhoto


class FSProjectsGateway(FSStorageGateway, ProjectGateway):  # type: ignore
    _KEY: str = 'projects'

    def _serialize_media(self, data: List[Dict[str, str]]) -> List[ProjectPhoto]:
        media: List[ProjectPhoto] = [
            ProjectPhoto(
                photo=photo["photo"],
            ) for photo in data
        ]
        return media

    def _serialize_project(self, project: Dict[str, Any]) -> Project:
        return Project(
            id=project["id"],
            name=project["name"],
            description=project["description"],
            media=self._serialize_media(project["media"]),
        )

    def add_project(self, project: Project) -> Project:
        self._fetch_db()
        project.id = self._get_next_id()
        self._memory.append(asdict(project))
        self._commit_changes()
        return project

    def get_projects(self) -> List[Project]:
        self._fetch_db()
        return [self._serialize_project(project) for project in self._memory]

    def get_project(self, project_id: int) -> Project:
        self._fetch_db()
        for project in self._memory:
            if project["id"] == project_id:
                return self._serialize_project(project)

        raise ValueError(f"Project №{project_id} not found.")


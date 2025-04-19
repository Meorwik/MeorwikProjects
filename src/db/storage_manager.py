from src.domain.project_manager import ProjectGateway
from src.domain.entities.project import Project, ProjectPhoto
from dataclasses import asdict
from typing import List, Dict
import json


class FSStorageGateway(ProjectGateway):

    def __init__(self):
        self._memory: List[Dict] = self._load_db()

    def _load_db(self):
        with open("db.json", "r") as db:
            return json.load(db)

    def _fetch_bd(self):
        self._memory = self._load_db()

    def _serialize_media(self, data: List[Dict]) -> List[ProjectPhoto]:
        media: List[ProjectPhoto] = [
            ProjectPhoto(
                photo=photo["photo"],
            ) for photo in data
        ]
        return media

    def _serialize_project(self, project: Dict) -> Project:
        return Project(
            id=project["id"],
            name=project["name"],
            description=project["description"],
            media=self._serialize_media(project["media"]),
        )

    def _get_next_id(self) -> int:
        if not self._memory:
            return 1
        return max(project["id"] for project in self._memory) + 1

    def _commit_changes(self) -> None:
        with open("db.json", "w") as f:
            json.dump(self._memory, f, indent=4)

    def add_project(self, project: Project) -> Project:
        self._fetch_bd()
        project.id = self._get_next_id()
        self._memory.append(asdict(project))
        self._commit_changes()
        return project

    def get_projects(self) -> List[Project]:
        self._fetch_bd()
        return [self._serialize_project(project) for project in self._memory]

    def get_project(self, project_id: int) -> Project:
        self._fetch_bd()
        for project in self._memory:
            if project["id"] == project_id:
                return self._serialize_project(project)

        raise ValueError(f"Project №{project_id} not found.")


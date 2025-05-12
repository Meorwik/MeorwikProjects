import json
from dataclasses import asdict
from typing import Dict, List

from src.domain.entities.project import Project, ProjectPhoto
from src.domain.project_manager import ProjectGateway

storage_data_type = Dict[str, str | int] # I will rename later
rename_later = List[storage_data_type] # Nikita if ur reading this, could you pls explain how should I name such context data types

class FSStorageGateway(ProjectGateway):

    def __init__(self) -> None:
        self._memory: rename_later = self._load_db()

    def _load_db(self) -> rename_later:
        with open("db.json", "r") as db:
            result: rename_later = json.load(db)
        return result

    def _fetch_bd(self) -> None:
        self._memory = self._load_db()

    def _serialize_media(self, data: rename_later) -> List[ProjectPhoto]:
        media: List[ProjectPhoto] = [
            ProjectPhoto(
                photo=photo["photo"],
            ) for photo in data
        ]
        return media

    def _serialize_project(self, project: storage_data_type) -> Project:
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


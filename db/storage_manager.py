from db.models.project import ProjectDb, ProjectPhotoDb
from domain.project_manager import ProjectsGateway
from typing import List, Dict
import json


class FSStorageGateway(ProjectsGateway):

    def __init__(self):
        self._memory: List[Dict] = self._load_db()

    def _load_db(self):
        with open("db.json", "r") as db:
            return json.load(db)

    def _fetch_bd(self):
        self._memory = self._load_db()

    def _serialize_media(self, data: List[Dict]) -> List[ProjectPhotoDb]:
        media: List[ProjectPhotoDb] = [
            ProjectPhotoDb(
                photo=photo["photo"],
            ) for photo in data
        ]
        return media

    def _serialize_projects(self, data: List[Dict]) -> List[ProjectDb]:
        projects: List[ProjectDb] = [
            ProjectDb(
                id=project["id"],
                name=project["name"],
                description=project["description"],
                media=self._serialize_media(project["media"]),
            ) for project in data
        ]

        return projects

    def _get_next_id(self) -> int:
        ...

    def _commit_changes(self) -> None:
        with open("db.json", "w") as f:
            json.dump(self._memory, f, indent=4)

    def add_project(self, project: ProjectDb) -> None:
        self._fetch_bd()
        self._memory.append(project.as_dict())
        self._commit_changes()

    def get_projects(self) -> List[ProjectDb]:
        self._fetch_bd()
        projects: List[ProjectDb] = self._serialize_projects(self._memory)
        return projects

    def get_project(self, project_id: int) -> Project:
        self._fetch_bd()
        for project in self._memory:
            if project.id == project_id:
                return project


class DBStorageGateway(ProjectsGateway):
    def add_projects(self, project: ProjectDb) -> :

    def get_projects(self) -> List[ProjectDb]:
        ...

    def get_project(self, project_id: int) -> ProjectDb:
        ...

    def add_project(self, project: ProjectDb):
        ...
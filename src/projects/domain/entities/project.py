from dataclasses import dataclass
from typing import List


@dataclass
class BaseEntity:
    ...


@dataclass
class ProjectPhoto(BaseEntity):
    photo: str


@dataclass
class Project(BaseEntity):
    name: str
    description: str
    media: List[ProjectPhoto]
    id: int | None = None

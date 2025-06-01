from dataclasses import dataclass
from typing import List


@dataclass
class ProjectPhoto:
    photo: str


@dataclass
class Project:
    name: str
    description: str
    media: List[ProjectPhoto]
    id: int | None = None

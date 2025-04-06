from dataclasses import dataclass, asdict
from typing import List


@dataclass
class BaseEntity:

    def as_dict(self):
        return asdict(self)

@dataclass
class ProjectPhoto(BaseEntity):
    photo: str


@dataclass
class Project(BaseEntity):
    id: int
    name: str
    description: str
    media: List[ProjectPhoto]

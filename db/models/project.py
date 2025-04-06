from dataclasses import dataclass, asdict
from typing import List


@dataclass
class DbModel:

    def as_dict(self):
        return asdict(self)


@dataclass
class ProjectPhotoDb(DbModel):
    photo: str



@dataclass
class ProjectDb(DbModel):
    name: str
    description: str
    media: List[ProjectPhotoDb]
    id: int = None



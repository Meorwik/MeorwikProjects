from dataclasses import dataclass, asdict
from pydantic import BaseModel
from typing import List

@dataclass
class BaseEntity:

    def as_dict(self):
        return asdict(self)


class ProjectPhotoCreate(BaseModel):
    photo: str


class ProjectPhotoResponse(BaseEntity):
    photo: str


class ProjectCreate(BaseModel):
    name: str
    description: str
    media: List[ProjectPhotoCreate]


class ProjectResponse(ProjectCreate):
    id: int
    media: List[ProjectPhotoResponse]

    class Config:
        orm_mode = True
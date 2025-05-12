from dataclasses import dataclass
from typing import List

from pydantic import BaseModel


@dataclass
class BaseEntity:
    ...

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
        from_attributes = True
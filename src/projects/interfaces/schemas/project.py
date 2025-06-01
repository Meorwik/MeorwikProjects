from typing import List

from pydantic import BaseModel


class ProjectPhoto(BaseModel):
    photo: str


class ProjectCreate(BaseModel):
    name: str
    description: str
    media: List[ProjectPhoto]


class ProjectResponse(BaseModel):
    id: int
    media: List[ProjectPhoto]

    class Config:
        from_attributes = True

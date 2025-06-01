from dataclasses import dataclass

from .enums import Roles


@dataclass
class User:
    name: str
    email: str
    password: str
    role: Roles = Roles.user
    id: int | None = None

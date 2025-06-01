from dataclasses import dataclass

from projects.domain.entities.enums import Roles


@dataclass
class User:
    name: str
    email: str
    password: str
    role: Roles = Roles.user.value
    id: int | None = None



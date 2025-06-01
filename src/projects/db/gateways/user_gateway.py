from dataclasses import asdict
from typing import Any, Dict, List

from projects.db.gateways.base import FSStorageGateway
from projects.domain.entities import User
from projects.domain.entities.enums import Roles
from projects.domain.protocols import UsersGateway


class FSUserGateway(FSStorageGateway, UsersGateway):  # type: ignore
    _KEY: str = "users"

    def _serialize_user(self, user: Dict[str, Any]) -> User:
        return User(
            id=user["id"],
            name=user["name"],
            email=user["email"],
            password=user["password"],
            role=Roles(user["role"]),
        )

    def get_user(self, user_id: int) -> User:
        self._fetch_db()
        for user in self._memory:
            if user["id"] == user_id:
                return self._serialize_user(user)

        raise ValueError(f"User №{user_id} not found.")

    def add_user(self, user: User) -> User:
        self._fetch_db()
        user.id = self._get_next_id()
        self._memory.append(asdict(user))
        self._commit_changes()
        return user

    def get_users(self) -> List[User]:
        self._fetch_db()
        return [self._serialize_user(user) for user in self._memory]

    def remove_user(self, user_id: int) -> bool:
        self._fetch_db()
        for user in self._memory:
            if user["id"] == user_id:
                try:
                    self._memory.remove(user)
                    self._commit_changes()
                except Exception as e:
                    raise ValueError(f"Failed to remove user cuz of {e}")

        return True

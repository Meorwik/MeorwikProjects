from json import dump, load
from typing import Any, Dict, List

from projects.domain.protocols import FSGateway


class FSStorageGateway(FSGateway):  # type: ignore
    _KEY: str = "projects"

    def __init__(self) -> None:
        self._memory: List[Dict[str, str | int]] = self._load_db()

    def _load_db(self) -> List[Dict[str, str | int]]:
        with open("db.json", "r") as db:
            result: List[Dict[str, str | int]] = load(db)[self._KEY]
        return result

    def _fetch_db(self) -> None:
        self._memory = self._load_db()

    def _get_next_id(self) -> int:
        if not self._memory:
            return 1
        return max(int(item["id"]) for item in self._memory) + 1

    def _commit_changes(self) -> None:
        with open("db.json", "r") as db:
            full_data: Dict[str, Any] = load(db)
        full_data[self._KEY] = self._memory
        with open("db.json", "w") as f:
            dump(full_data, f, indent=4)

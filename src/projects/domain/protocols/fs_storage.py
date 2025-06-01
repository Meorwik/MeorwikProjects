from typing import Any, Dict, List, Protocol


class FSGateway(Protocol):
    def _load_db(self) -> List[Dict[str, Any]]: ...

    def _fetch_db(self) -> None: ...

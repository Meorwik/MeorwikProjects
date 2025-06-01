from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from projects.main import app


@pytest.fixture(scope="session")
def client() -> Iterator[TestClient]:
    with TestClient(app) as client:
        yield client

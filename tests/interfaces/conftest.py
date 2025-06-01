from typing import Generator

import pytest
from fastapi.testclient import TestClient
from pytest import fixture

from projects.main import app


@pytest.fixture(scope="session")
def client() -> Generator[TestClient]:
    with TestClient(app) as client:
        yield client

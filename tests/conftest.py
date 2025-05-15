import pytest

from projects.db import FSStorageGateway
from projects.domain import ProjectGateway


@pytest.fixture(scope="session")
def gateway() -> ProjectGateway:
    return FSStorageGateway()
import pytest

from src.db.storage_manager import FSStorageGateway
from src.domain.project_manager import ProjectGateway


@pytest.fixture(scope="session")
def gateway() -> ProjectGateway:
    return FSStorageGateway()
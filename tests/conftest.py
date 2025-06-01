import pytest

from projects.db.gateways.storage_gateway import FSProjectsGateway
from projects.domain.protocols.projects_protocol import ProjectGateway


@pytest.fixture(scope="session")
def gateway() -> ProjectGateway:
    return FSProjectsGateway()

from projects.domain import ProjectGateway


def test_get_projects_returns_expected_data(gateway: ProjectGateway) -> None:
    result = gateway.get_projects()

    assert isinstance(result, list)
    assert len(result) > 0




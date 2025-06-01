from fastapi.testclient import TestClient


def test_get_projects(client: TestClient) -> None:
    result = client.get("/projects/")
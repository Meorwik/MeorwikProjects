from fastapi.testclient import TestClient


def test_get_projects(client: TestClient) -> None:
    client.get("/projects/")

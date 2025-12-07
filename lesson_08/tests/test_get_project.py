from lesson_08.API.projects_api import ProjectsAPI


def test_get_project_positive(projects_api: ProjectsAPI):
    # создаём проект для теста
    create_resp = projects_api.create_project("Project for GET")
    project_id = create_resp.json()["id"]

    response = projects_api.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Project for GET"


def test_get_project_negative_wrong_id(projects_api: ProjectsAPI):
    response = projects_api.get_project(99999999)
    assert response.status_code == 404

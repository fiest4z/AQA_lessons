from lesson_08.API.projects_api import ProjectsAPI


def test_update_project_positive(projects_api: ProjectsAPI):
    create_resp = projects_api.create_project("Project for Update")
    project_id = create_resp.json()["id"]

    response = projects_api.update_project(project_id, "Updated Title")
    assert response.status_code == 200

    get_resp = projects_api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Updated Title"


def test_update_project_negative_invalid_id(projects_api: ProjectsAPI):
    response = projects_api.update_project(99999999, "New Title")
    assert response.status_code == 404

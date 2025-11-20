from lesson_08.API.projects_api import ProjectsAPI



def test_create_project_positive(projects_api: ProjectsAPI):
    response = projects_api.create_project("Test Project")
    assert response.status_code == 201
    data = response.json()
    assert "id" in data

def test_create_project_negative_empty_title(projects_api: ProjectsAPI):
    response = projects_api.create_project("")
    assert response.status_code == 400

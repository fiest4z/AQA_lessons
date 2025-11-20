import pytest
from lesson_08.API.projects_api import ProjectsAPI  # Добавьте этот импорт

BASE_URL = "https://yougile.com"

@pytest.fixture(scope="session")
def token():
    # Ваш реальный токен
    return "TOKEN"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def projects_api(token, base_url):
    return ProjectsAPI(base_url, token)
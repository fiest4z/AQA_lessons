from .client import Client


class ProjectsAPI:
    def __init__(self, base_url, token):
        self.client = Client(base_url, token)

    def create_project(self, title):
        body = {
            "title": title
        }
        return self.client.post("/api-v2/projects", body)

    def get_project(self, project_id):
        return self.client.get(f"/api-v2/projects/{project_id}")

    def update_project(self, project_id, title):
        body = {
            "title": title
        }
        return self.client.put(f"/api-v2/projects/{project_id}", body)
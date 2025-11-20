import requests


class Client:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        print(f"Client initialized with token: {token[:10]}...")

    def post(self, endpoint, json_data=None):
        print(f"POST {self.base_url}{endpoint}")
        print(f"Body: {json_data}")

        response = requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=json_data
        )

        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        return response

    def get(self, endpoint):
        print(f"GET {self.base_url}{endpoint}")

        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        )

        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        return response

    def put(self, endpoint, json_data=None):
        print(f"PUT {self.base_url}{endpoint}")
        print(f"Body: {json_data}")

        response = requests.put(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=json_data
        )

        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        return response
from unittest import TestCase

from fastapi.testclient import TestClient
from main import app


class MainTestCase(TestCase):
    def test_root(self):
        client = TestClient(app)

        response = client.get("/")

        self.assertEqual(response.status_code, 200)

        self.assertIs(type(response.json()), dict)

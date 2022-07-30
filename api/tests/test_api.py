import unittest
from http import HTTPStatus
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


class TestApiResponses(unittest.TestCase):

    def test_status(self):
        """ GET /status
        Indicate the service has started up correctly
         and is ready to accept requests.
        Responses:
        200 OK When the service is ready to receive requests."""
        response = client.get('/status')
        self.assertEqual(response.status_code, HTTPStatus.OK)
import json
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
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_put_cars(self):
        """ PUT /cars
        Load the list of available cars in the service and remove all previous data
        (existing journeys and cars).
        This method may be called more than once during the life cycle of the service.
        Body required The list of cars to load.
        Content Type application/json

        Responses:

        200 OK When the list is registered correctly.
        400 Bad Request When there is a failure in the request format, expected headers,
         or the payload can't be unmarshalled.
        """
        with open('data_provider/cars.json') as file:
            cars = json.load(file)
        response = client.put('/cars',
                              headers={'Content-Type': 'application/json'},
                              json=cars)

        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_put_cars_without_content_type(self):
        with open('data_provider/cars.json') as file:
            cars = json.load(file)
        response = client.put('/cars',
                              headers={'Content-Type': ''},
                              json=cars)

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)

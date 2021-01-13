import unittest
from unittest.mock import patch

from mathapi.app import create_app


class TestFibonacciResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app(environment="testing")
        self.client = self.app.test_client

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.requests.save")
    def test_valid_data(self, _save):
        # test happy path in integration
        response = self.client().post("/api/v1/factorial", json={"number": 5})

        assert response.json == {"result": 120}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.factorial.factorial", lambda n: 120)
    @patch("mathapi.services.requests.save")
    def test_save_request(self, save):
        self.client().post("/api/v1/factorial", json={"number": 5})

        save.assert_called_with("fac", 5)

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.factorial.factorial")
    @patch("mathapi.services.requests.save")
    def test_non_integer_number(self, save, factorial):
        response = self.client().post("/api/v1/factorial", json={"number": "invalid"})

        save.assert_not_called()
        factorial.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "The number must be an integer number"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.factorial.factorial")
    @patch("mathapi.services.requests.save")
    def test_negative_number(self, save, factorial):
        response = self.client().post("/api/v1/factorial", json={"number": -1})

        save.assert_not_called()
        factorial.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "Factorial not defined for negative values"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.factorial.factorial")
    @patch("mathapi.services.requests.save")
    def test_large_number(self, save, factorial):
        response = self.client().post("/api/v1/factorial", json={"number": 10e6})

        save.assert_not_called()
        factorial.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "The number is too large"}}

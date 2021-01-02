import unittest
from unittest.mock import patch

from mathapi.app import create_app


class TestFibonacciResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app(test_config=True)
        self.client = self.app.test_client

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.requests.save")
    def test_valid_data(self, _save):
        # test happy path in integration
        response = self.client().post("/api/v1/fibonacci", json={"number": 10})

        assert response.json == {"result": 55}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.fibonacci.nth_fibonacci", lambda n: 55)
    @patch("mathapi.services.requests.save")
    def test_save_request(self, save):
        self.client().post("/api/v1/fibonacci", json={"number": 10})

        save.assert_called_with("fib", 10)

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.fibonacci.nth_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_non_integer_number(self, save, nth_fibonacci):
        response = self.client().post("/api/v1/fibonacci", json={"number": "invalid"})

        save.assert_not_called()
        nth_fibonacci.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "The number must be an integer number"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.fibonacci.nth_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_negative_number(self, save, nth_fibonacci):
        response = self.client().post("/api/v1/fibonacci", json={"number": -1})

        save.assert_not_called()
        nth_fibonacci.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "The number must be a non-negative integer"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.fibonacci.nth_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_large_number(self, save, nth_fibonacci):
        response = self.client().post("/api/v1/fibonacci", json={"number": 1e10})

        save.assert_not_called()
        nth_fibonacci.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "The number is too large"}}

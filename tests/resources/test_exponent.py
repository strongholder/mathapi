import unittest
from unittest.mock import patch

from mathapi.app import create_app


class TestExponentResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app(test_config=True)
        self.client = self.app.test_client

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.requests.save")
    def test_valid_data(self, _save):
        # test happy path in integration
        response = self.client().post("/api/v1/exponent", json={"base": 2, "exponent": 3})

        assert response.json == {"result": 8}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.exponent.power", new=lambda b, e: 8)
    @patch("mathapi.services.requests.save")
    def test_save_request(self, save):
        self.client().post("/api/v1/exponent", json={"base": 2, "exponent": 3})

        save.assert_called_with("exp", 2, 3)

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.exponent.power")
    @patch("mathapi.services.requests.save")
    def test_non_integer_base(self, save, power):
        response = self.client().post("/api/v1/exponent", json={"base": "invalid", "exponent": 3})

        save.assert_not_called()
        power.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"base": "The base must be an integer number"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.exponent.power")
    @patch("mathapi.services.requests.save")
    def test_large_base(self, save, power):
        response = self.client().post("/api/v1/exponent", json={"base": 1e15, "exponent": 3})

        save.assert_not_called()
        power.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"base": "The base is too large"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.exponent.power")
    @patch("mathapi.services.requests.save")
    def test_non_integer_exponent(self, save, power):
        response = self.client().post("/api/v1/exponent", json={"base": 2, "exponent": "invalid"})

        save.assert_not_called()
        power.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"exponent": "The exponent must be an integer number"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.exponent.power")
    @patch("mathapi.services.requests.save")
    def test_large_exponent(self, save, power):
        response = self.client().post("/api/v1/exponent", json={"base": 2, "exponent": 2e5})

        save.assert_not_called()
        power.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"exponent": "The exponent is too large"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.requests.save")
    def test_raise_zero_to_negative_power(self, save):
        response = self.client().post("/api/v1/exponent", json={"base": 0, "exponent": -2})

        assert response.json == {"message": "0 cannot be raised to a negative number"}

    @patch("mathapi.services.exponent.power")
    @patch("mathapi.services.requests.save")
    def test_unauthorized(self, save, power):
        response = self.client().post("/api/v1/exponent", json={"base": 2, "exponent": 3})

        save.assert_not_called()
        power.assert_not_called()
        assert response.status_code == 401

import base64
import unittest
from unittest.mock import Mock, patch

from mathapi.app import create_app
from mathapi.models import Request
from mathapi.testing import db_test


class TestExponentResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app(test_config=True)

        self._headers = {"Authorization": f"Basic {base64.b64encode(b'test:password').decode('utf-8')}"}
        self.client = self.app.test_client()

    def test_exponent(self):
        with db_test(self.app):
            response = self.client.post("/api/v1/exponent", json={"base": 2, "exponent": 3}, headers=self._headers)

            assert Request.query.filter_by(operation="exp", arg1=2, arg2=3).first() is not None
            assert response.status_code == 200
            assert response.json == {"result": 8}

    def test_factorial(self):
        with db_test(self.app):
            response = self.client.post("/api/v1/factorial", json={"number": 5}, headers=self._headers)

            assert Request.query.filter_by(operation="fac", arg1=5, arg2=None).first() is not None
            assert response.status_code == 200
            assert response.json == {"result": 120}

    def test_fibonacci(self):
        with db_test(self.app):
            response = self.client.post("/api/v1/fibonacci", json={"number": 10}, headers=self._headers)

            assert Request.query.filter_by(operation="fib", arg1=10, arg2=None).first() is not None
            assert response.status_code == 200
            assert response.json == {"result": 55}

    @patch("flask_mail.Message")
    @patch("mathapi.app.mail")
    def test_fibonacci_async(self, mail, message):
        with db_test(self.app):
            message_object = Mock()
            message.return_value = message_object

            response = self.client.post(
                "/api/v1/fibonacci_async", json={"number": 10, "email": "test@example.com"}, headers=self._headers
            )
            request = Request.query.filter_by(operation="fib", arg1=10, arg2=None).first()

            message.assert_called_with(
                subject="Fib(10) result",
                body="Please find your result as a file attached to this messages.",
                recipients=["test@example.com"],
            )
            message_object.attach.assert_called_with("result.txt", "text/plain", "55")
            mail.send.assert_called_with(message_object)

            assert request is not None
            assert request.completed is True
            assert response.status_code == 201
            assert response.json == ""

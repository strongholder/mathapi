import base64
import unittest

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

import unittest
from unittest.mock import patch

from mathapi.app import create_app


class TestFibonacciAsyncResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app(environment="testing")
        self.client = self.app.test_client
        self.email = "test@example.com"

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.celery.tasks.compute_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_valid_data(self, _save, _compute_fibonacci_task):
        # test happy path in integration
        response = self.client().post("/api/v1/fibonacci_async", json={"number": 10, "email": self.email})

        assert response.json == ""
        assert response.status_code == 201

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.fibonacci.nth_fibonacci", lambda n: 55)
    @patch("mathapi.celery.tasks.compute_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_save_request(self, save, _compute_fibonacci_task):
        self.client().post("/api/v1/fibonacci_async", json={"number": 10, "email": self.email})

        save.assert_called_with("fib", 10, email=self.email)

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.services.fibonacci.nth_fibonacci", lambda n: 55)
    @patch("mathapi.services.requests.save", lambda *a, **kw: 42)
    @patch("mathapi.celery.tasks.compute_fibonacci")
    def test_invoke_async_task(self, compute_fibonacci_task):
        self.client().post("/api/v1/fibonacci_async", json={"number": 10, "email": self.email})

        compute_fibonacci_task.apply_async.assert_called_with(args=[42])

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.celery.tasks.compute_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_non_integer_number(self, save, compute_fibonacci_task):
        response = self.client().post("/api/v1/fibonacci_async", json={"number": "invalid"})

        save.assert_not_called()
        compute_fibonacci_task.apply_async.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "The number must be an integer number"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.celery.tasks.compute_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_negative_number(self, save, compute_fibonacci_task):
        response = self.client().post("/api/v1/fibonacci_async", json={"number": -1})

        save.assert_not_called()
        compute_fibonacci_task.apply_async.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "The number must be a non-negative integer"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.celery.tasks.compute_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_large_number(self, save, compute_fibonacci_task):
        response = self.client().post("/api/v1/fibonacci_async", json={"number": 10e10})

        save.assert_not_called()
        compute_fibonacci_task.apply_async.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"number": "The number is too large"}}

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.celery.tasks.compute_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_missing_email(self, save, compute_fibonacci_task):
        response = self.client().post("/api/v1/fibonacci_async", json={"number": 10})

        save.assert_not_called()
        compute_fibonacci_task.apply_async.assert_not_called()
        assert response.status_code == 400
        assert response.json == {
            "message": {"email": "Missing required parameter in the JSON body or the post body or the query string"}
        }

    @patch("mathapi.services.auth.authenticate", new=lambda: True)
    @patch("mathapi.celery.tasks.compute_fibonacci")
    @patch("mathapi.services.requests.save")
    def test_invalid_email(self, save, compute_fibonacci_task):
        response = self.client().post("/api/v1/fibonacci_async", json={"number": 10, "email": "gibber@ish"})

        save.assert_not_called()
        compute_fibonacci_task.apply_async.assert_not_called()
        assert response.status_code == 400
        assert response.json == {"message": {"email": "Invalid email address"}}

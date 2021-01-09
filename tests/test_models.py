import unittest

from mathapi.app import create_app, db
from mathapi.models import Request
from mathapi.testing import db_test


class TestRequest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(test_config=True)

    def test_complete(self):
        with db_test(self.app):
            request = Request(operation="fib", arg1=4, asynchronous=True, email="test@example.com")
            db.session.add(request)
            db.session.commit()
            request.complete()

            assert Request.query.filter_by(operation="fib", asynchronous=True, completed=True).first() is not None

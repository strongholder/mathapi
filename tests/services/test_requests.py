from mathapi.models import Request
from mathapi.services.requests import save
from mathapi.testing import db_test


def test_save_request():
    with db_test():
        save("exp", 10e12, -200)
        save("fac", 10e5)
        save("fib", 10e6)
        save("fib", 10e6, email="test@example.com")

        assert (
            Request.query.filter_by(operation="exp", arg1=10e12, arg2=-200, asynchronous=False, email=None).first()
            is not None
        )
        assert (
            Request.query.filter_by(operation="fac", arg1=10e5, arg2=None, asynchronous=False, email=None).first()
            is not None
        )
        assert (
            Request.query.filter_by(operation="fib", arg1=10e6, arg2=None, asynchronous=False, email=None).first()
            is not None
        )
        assert (
            Request.query.filter_by(
                operation="fib", arg1=10e6, arg2=None, asynchronous=True, email="test@example.com"
            ).first()
            is not None
        )

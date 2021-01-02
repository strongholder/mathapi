from mathapi.models import Request
from mathapi.services.requests import save
from mathapi.testing import db_test


def test_save_request():
    with db_test():
        save("exp", 10e12, -200)
        save("fib", 10e6)
        save("fac", 10e5)

        assert Request.query.filter_by(operation="exp", arg1=10e12, arg2=-200).first() is not None
        assert Request.query.filter_by(operation="fib", arg1=10e6, arg2=None).first() is not None
        assert Request.query.filter_by(operation="fac", arg1=10e5, arg2=None).first() is not None

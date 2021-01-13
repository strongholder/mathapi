import contextlib

from mathapi.app import create_app, db


@contextlib.contextmanager
def db_test(app=None):
    if app is None:
        app = create_app(environment="testing")

    with app.app_context():
        # create all tables
        db.create_all()

        yield app

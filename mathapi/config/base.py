import importlib
import os


class EnvironmentError(Exception):
    pass


class Config:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_USER = "mathapi"
    API_PASSWORD = os.getenv(
        "MATHAPI_PASSWORD",
        "pbkdf2:sha256:150000$vpf8o9kq$961dcfbd582de375f85126cf3686ba61b9add54d18374a0eb38ac359085cff96",
    )
    SENTRY_DSN = "http://82b2524c7dfe4a8eafb2a7fafa2d1e84@mathapi-sentry-relay:3000/2"


def load(app):
    if app.env not in ["development", "production", "testing", "staging"]:
        raise EnvironmentError("Unknown environment: Please check your FLASK_ENV environment variable")

    config_module = importlib.import_module(f"mathapi.config.{app.env}")
    config = config_module.Config()

    app.config.from_object(config)

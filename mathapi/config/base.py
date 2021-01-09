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
    SENTRY_DSN = "http://4bbed19ccdae497e9dcdd62d53f9b2c6@mathapi-sentry-relay:3000/2"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = "587"
    MAIL_USERNAME = "noreply.mathapi@gmail.com"
    MAIL_PASSWORD = os.getenv("SMTP_PASSWORD")
    MAIL_DEFAULT_SENDER = "noreply.mathapi@gmail.com"
    MAIL_USE_TLS = True

    broker_url = "redis://localhost:6379/0"
    result_backend = "redis://localhost:6379/0"


def load(app):
    config = load_object(app)
    app.config.from_object(config)


def load_object(app):
    if app.env not in ["development", "production", "testing", "staging"]:
        raise EnvironmentError("Unknown environment: Please check your FLASK_ENV environment variable")

    config_module = importlib.import_module(f"mathapi.config.{app.env}")
    config = config_module.Config()

    return config

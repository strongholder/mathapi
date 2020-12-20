import importlib


class EnvironmentError(Exception):
    pass


class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = "sqlite:///:memory:"


def load(app):
    if app.env not in ["development", "production", "testing", "staging"]:
        raise EnvironmentError("Unknown environment: Please check your FLASK_ENV environment variable")

    config_module = importlib.import_module(f"mathapi.config.{app.env}")
    config = config_module.Config()

    app.config.from_object(config)

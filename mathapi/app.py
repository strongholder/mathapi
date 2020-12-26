import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from mathapi import config
from mathapi.resources import api, api_metrics


def create_app(test_config=None):
    app = Flask(__name__)
    config.load(app)

    sentry_sdk.init(
        dsn=app.config["SENTRY_DSN"],
        integrations=[FlaskIntegration()],
        environment=app.env,
        traces_sample_rate=1.0,
    )

    @app.route("/")
    def index():
        return "Hello, we will add a web client soon!"

    @app.route("/health_check")
    def health_check():
        return ("", 200)

    api.init_app(app)
    api_metrics.init_app(app, api)

    return app

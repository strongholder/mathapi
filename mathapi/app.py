import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from mathapi import config
from mathapi.resources import api, api_metrics


def create_app(test_config=None):
    sentry_sdk.init(
        dsn="http://82b2524c7dfe4a8eafb2a7fafa2d1e84@mathapi-sentry-relay:3000/2",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
    )
    app = Flask(__name__)
    config.load(app)

    @app.route("/")
    def index():
        return "Hello, we will add a web client soon!"

    @app.route("/health_check")
    def health_check():
        return ("", 200)

    api.init_app(app)
    api_metrics.init_app(app, api)

    return app

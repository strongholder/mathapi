import os
import pathlib

import sentry_sdk
from flask import Flask, send_file, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sentry_sdk.integrations.flask import FlaskIntegration

from mathapi import config
from mathapi.resources import api, api_metrics
from mathapi.services.auth import login_required

db = SQLAlchemy()
migrate = Migrate(compare_type=True)


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.env = "testing"

    config.load(app)

    sentry_sdk.init(
        dsn=app.config["SENTRY_DSN"],
        integrations=[FlaskIntegration()],
        environment=app.env,
        traces_sample_rate=1.0,
    )
    db.init_app(app)
    migrate.init_app(app, db)

    public_dir = os.path.join(app.config["BASE_DIR"], "client", "public")

    @app.route("/")
    @login_required
    def index():
        return send_from_directory(public_dir, "index.html")

    @app.route("/app/<path:path>")
    def app_path(path):
        return send_file(pathlib.Path(public_dir) / path)

    @api_metrics.exclude_all_metrics()
    @app.route("/health_check")
    def health_check():
        return ("", 200)

    api.init_app(app)
    api_metrics.init_app(app, api)
    from mathapi.models import Request

    return app

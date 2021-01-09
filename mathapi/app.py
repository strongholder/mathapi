import sentry_sdk
from celery import Celery
from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sentry_sdk.integrations.flask import FlaskIntegration

from mathapi import config
from mathapi.celery import init_celery
from mathapi.resources import api, api_metrics
from mathapi.views import views

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
celery = Celery()
mail = Mail()


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
    init_celery(app, celery)
    mail.init_app(app)

    app.register_blueprint(views)

    api.init_app(app)
    api_metrics.init_app(app, api)
    from mathapi.models import Request

    return app


if __name__ == "__main__":
    app = create_app()
    celery = init_celery(app, celery)

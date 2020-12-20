from flask import Flask

from mathapi import config


def create_app(test_config=None):
    app = Flask(__name__)
    config.load(app)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app

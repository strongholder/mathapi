import base64
from functools import lru_cache, wraps

import flask
import flask_restful
from werkzeug.exceptions import Unauthorized
from werkzeug.security import check_password_hash


@lru_cache
def users():
    config = flask.current_app.config
    users = {
        config["API_USER"]: config["API_PASSWORD"],
    }

    return users


def verify_password(username, password):
    if username in users() and check_password_hash(users().get(username), password):
        return username


def authenticate():
    headers = flask_restful.request.headers
    authorization = headers.get("Authorization", "")

    if "basic" not in authorization.lower():
        return None

    username, password = base64.b64decode(authorization.split()[-1]).decode("utf-8").split(":")
    return verify_password(username, password)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        acct = authenticate()

        if acct:
            return func(*args, **kwargs)

        raise Unauthorized(www_authenticate='Basic realm="Please provide valid credentials"')

    return wrapper

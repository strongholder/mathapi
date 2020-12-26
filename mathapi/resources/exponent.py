from flask_restful import reqparse

from mathapi.resources.api_resource import ApiResource
from mathapi.services import requests
from mathapi.services.exponent import power

MAX_BASE = 10e12
MAX_EXPONENT = 10e4


def base_integer(base):
    try:
        base = int(base)
    except ValueError:
        raise ValueError("The base must be an integer number")

    if base > MAX_BASE:
        raise ValueError("The base is too large")

    return base


def exponent_integer(exponent):
    try:
        exponent = int(exponent)
    except ValueError:
        raise ValueError("The exponent must be an integer number")

    if exponent > MAX_EXPONENT:
        raise ValueError("The exponent is too large")

    return exponent


parser = reqparse.RequestParser()
parser.add_argument("base", type=base_integer, required=True)
parser.add_argument("exponent", type=exponent_integer, required=True)


class Exponent(ApiResource):
    def post(self):
        args = parser.parse_args()
        requests.save("exp", args["base"], args["exponent"])
        return {"result": power(args["base"], args["exponent"])}

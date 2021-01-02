"""
Compute the power given an integer base and exponent

Note: Although the power function supports floating point base and
exponent for simplicity in the API we only allow integers
"""
from flask_restful import abort, reqparse

from mathapi.resources.api_resource import ApiResource
from mathapi.services import requests
from mathapi.services.exponent import power

MAX_BASE = 10e12
MAX_EXPONENT = 10e4


def validate_args(base, exponent):
    if base == 0 and exponent < 0:
        abort(400, message="0 cannot be raised to a negative number")


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
        base, exponent = args["base"], args["exponent"]
        validate_args(base, exponent)

        requests.save("exp", base, exponent)
        return {"result": power(base, exponent)}

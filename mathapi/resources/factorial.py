"""
Compute the factorial for a given integer
"""

from flask_restful import reqparse

from mathapi.resources.api_resource import ApiResource
from mathapi.services import requests
from mathapi.services.factorial import factorial

MAX_NUMBER = 10e5


def number_integer(number):
    try:
        number = int(number)
    except ValueError:
        raise ValueError("The number must be an integer number")

    if number < 0:
        raise ValueError("Factorial not defined for negative values")

    if number > MAX_NUMBER:
        raise ValueError("The number is too large")

    return number


parser = reqparse.RequestParser()
parser.add_argument("number", type=number_integer, required=True)


class Factorial(ApiResource):
    def post(self):
        args = parser.parse_args()
        requests.save("fac", args["number"])
        return {"result": factorial(args["number"])}

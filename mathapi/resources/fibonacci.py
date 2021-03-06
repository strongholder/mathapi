"""
Compute the fibonacci sequence number for a given integer position
"""

from flask_restful import reqparse

from mathapi.resources.api_resource import ApiResource
from mathapi.services import requests
from mathapi.services.fibonacci import nth_fibonacci

MAX_NUMBER = 10e6


def number_integer(number):
    try:
        number = int(number)
    except ValueError:
        raise ValueError("The number must be an integer number")

    if number < 0:
        raise ValueError("The number must be a non-negative integer")

    if number > MAX_NUMBER:
        raise ValueError("The number is too large")

    return number


parser = reqparse.RequestParser()
parser.add_argument("number", type=number_integer, required=True)


class Fibonacci(ApiResource):
    def post(self):
        args = parser.parse_args()
        requests.save("fib", args["number"])
        return {"result": nth_fibonacci(args["number"])}

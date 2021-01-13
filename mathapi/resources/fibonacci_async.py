"""
Compute the fibonacci sequence number for a given integer position and
deliver the result over email. Allows for larger N than the synchronous implementation
"""
import re

from flask_restful import reqparse

from mathapi.resources.api_resource import ApiResource
from mathapi.services import requests

MAX_NUMBER = 10e8


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


def email_address(email):
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return email
    raise ValueError("Invalid email address")


parser = reqparse.RequestParser()
parser.add_argument("number", type=number_integer, required=True)
parser.add_argument("email", type=email_address, required=True)


class FibonacciAsync(ApiResource):
    def post(self):
        from mathapi.celery import tasks

        args = parser.parse_args()
        request_id = requests.save("fib", args["number"], email=args["email"])
        tasks.compute_fibonacci.apply_async(args=[request_id])
        return "", 201

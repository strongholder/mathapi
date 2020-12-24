from flask_restful import Resource, reqparse

from mathapi.services.factorial import factorial

MAX_NUMBER = 10 ** 5


def number_integer(number):
    try:
        number = int(number)
    except ValueError:
        raise ValueError("The number must be an integer number")

    if number > MAX_NUMBER:
        raise ValueError("The number is too large")

    return number


parser = reqparse.RequestParser()
parser.add_argument("number", type=number_integer, required=True)


class Factorial(Resource):
    def post(self):
        args = parser.parse_args()
        return {"result": factorial(args["number"])}

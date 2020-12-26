from flask_restful import Resource

from mathapi.services.auth import login_required


class ApiResource(Resource):
    method_decorators = [login_required]

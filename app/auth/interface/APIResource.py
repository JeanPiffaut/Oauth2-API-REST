from flask import request
from flask_restful import Resource

from app import response_structure
from app.common.interface.Miscellaneous import validate_headers


class APIResource(Resource):
    def get(self):
        valid = validate_headers(request.headers)
        if not valid:
            return valid

        return response_structure(404)

    def post(self):
        pass
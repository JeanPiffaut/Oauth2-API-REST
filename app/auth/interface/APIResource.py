from flask import request
from flask_restful import Resource

from app.common.interface.Miscellaneous import validate_headers


class APIResource(Resource):
    def get(self):
        valid = validate_headers(request.headers)
        if valid != True:
            print(2)
            return valid

        return {"message": "Hello World"}

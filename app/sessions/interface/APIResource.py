from flask_restful import Resource
from flask import request, abort

from app import response_structure


class SessionResource(Resource):

    def get(self):
        return response_structure(200)

    def post(self):
        return response_structure(200)

    def put(self):
        return response_structure(200)

    def delete(self):
        return response_structure(200)

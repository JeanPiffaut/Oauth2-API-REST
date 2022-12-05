from flask_restful import Resource
from flask import request, abort

from app import response_structure
from app.auth_types.application.ShowAuthType import ShowAuthType


class AuthTypeResource(Resource):

    def get(self):
        types = ShowAuthType()

        if request.args.get('id') is not None:
            types.setId(request.args.get('id'))

        if request.args.get('name') is not None:
            types.setName(request.args.get('name'))

        if request.args.get('client_id') is not None:
            types.setClientId(request.args.get('client_id'))

        if request.args.get('client_secret') is not None:
            types.setClientSecret(request.args.get('client_secret'))

        result = types.execute()
        return response_structure(200, result)

    def post(self):
        return response_structure(200)

    def put(self):
        return response_structure(200)

    def delete(self):
        return response_structure(200)

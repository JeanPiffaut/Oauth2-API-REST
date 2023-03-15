from decouple import config
from flask import request, abort
from flask_restful import Resource, reqparse

from app import response_structure
from app.common.interface.Miscellaneous import validate_headers
from app.credentials.application.ValidateCredentials import ValidateCredentials
from app.sessions.application.CreateSession import CreateSession


class APIResource(Resource):
    def get(self):
        valid = validate_headers(request.headers)
        if not valid:
            return valid

        return response_structure(404)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('password')
        parser.add_argument('auth_type')
        args = parser.parse_args()

        if args['username'] is None:
            abort(400)

        if args['password'] is None:
            abort(400)
        print(args)
        if args['auth_type'] is None:
            auth_type = config('DEFAULT_AUTH_TYPE')
        else:
            auth_type = args['auth_type']

        credential = ValidateCredentials()
        credentials = credential.execute(args['username'], args['password'], auth_type)
        if credentials is False:
            return response_structure(200, message="Usuario o contraseña incorrectas")

        session = CreateSession()
        session.setUserId(credentials['user'].id)
        result = session.execute()
        if result:
            return response_structure(201, {"token":session.getToken()})
        else:
            return response_structure(500)
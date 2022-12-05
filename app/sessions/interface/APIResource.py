from flask_restful import Resource
from flask import request, abort

from app import response_structure
from app.sessions.application.CreateSession import CreateSession


class SessionResource(Resource):

    def get(self):
        return response_structure(200)

    def post(self):
        if request.args.get('user_id') is None:
            abort(400)

        create = CreateSession()
        create.setUserId(request.args.get('user_id'))
        result = create.execute()
        if result:
            return response_structure(200)
        else:
            return response_structure(500)


    def put(self):
        return response_structure(200)

    def delete(self):
        return response_structure(200)

from flask_restful import Resource
from flask import request, abort

from app import response_structure
from app.credentials.application.CreateCredential import CreateCredential
from app.credentials.application.DeleteCredential import DeleteCredential
from app.credentials.application.ShowCredentials import ShowCredentials
from app.credentials.application.UpdateCredential import UpdateCredential


class CredentialResource(Resource):

    def get(self):
        show = ShowCredentials()

        if request.args.get('user_id') is not None:
            show.setUserId(request.args.get('user_id'))

        if request.args.get('auth_type') is not None:
            show.setAuthType(request.args.get('auth_type'))

        if request.args.get('username') is not None:
            show.setUsername(request.args.get('username'))

        if request.args.get('token') is not None:
            show.setToken(request.args.get('token'))

        result = show.execute(request.args.get('id'))
        return response_structure(200, result)

    def post(self):
        create = CreateCredential()

        if request.args.get('user_id') is None:
            abort(400)

        if request.args.get('auth_type') is None:
            abort(400)

        if request.args.get('username') is None:
            abort(400)

        if request.args.get('token') is None:
            abort(400)

        create.setUserId(request.args.get('user_id'))
        create.setAuthType(request.args.get('auth_type'))
        create.setUsername(request.args.get('username'))
        create.setToken(request.args.get('token'))
        result = create.execute()
        if result:
            return response_structure(200)
        else:
            return response_structure(500)

    def put(self):
        if request.args.get('id') is None:
            abort(400)

        update = UpdateCredential()

        if request.args.get('user_id') is not None:
            update.setUserId(request.args.get('user_id'))

        if request.args.get('auth_type') is not None:
            update.setAuthType(request.args.get('auth_type'))

        if request.args.get('username') is not None:
            update.setUsername(request.args.get('username'))

        if request.args.get('token') is not None:
            update.setToken(request.args.get('token'))

        result = update.execute(request.args.get('id'))
        if result:
            return response_structure(200)
        else:
            return response_structure(500)

    def delete(self):
        if request.args.get('id') is None:
            abort(400)

        delete = DeleteCredential()

        result = delete.execute(request.args.get('id'))
        if result:
            return response_structure(200)
        else:
            return response_structure(500)

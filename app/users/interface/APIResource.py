from flask_restful import Resource
from flask import request, abort

from app import response_structure
from app.credentials.application.DeleteCredential import DeleteCredential
from app.credentials.application.ShowCredentials import ShowCredentials
from app.sessions.application.DeleteSession import DeleteSession
from app.sessions.application.ShowSessions import ShowSessions
from app.users.application.CreateUser import CreateUser
from app.users.application.DeleteUser import DeleteUser
from app.users.application.ShowUsers import ShowUsers
from app.users.application.UpdateUser import UpdateUser


class UserResource(Resource):

    def get(self):
        users = ShowUsers()

        if request.args.get('name') is not None:
            users.setName(request.args.get('name'))

        if request.args.get('email') is not None:
            users.setEmail(request.args.get('email'))

        result = users.execute(request.args.get('id'))
        return response_structure(200, result)

    def post(self):
        if request.args.get('name') is None:
            abort(400)

        if request.args.get('email') is None:
            abort(400)

        create = CreateUser()
        create.setName(request.args.get('name'))
        create.setEmail(request.args.get('email'))

        result = create.execute()
        if result:
            return response_structure(201)
        else:
            return response_structure(500)

    def put(self):
        update = UpdateUser()

        if request.args.get('name') is not None:
            update.setName(request.args.get('name'))

        if request.args.get('email') is not None:
            update.setEmail(request.args.get('email'))

        result = update.execute(request.args.get('id'))
        if result:
            return response_structure(200)
        else:
            return response_structure(500)

    def delete(self):
        if request.args.get('id') is None:
            abort(400)

        user_id = request.args.get('id')

        delete_user = DeleteUser()
        result = delete_user.execute(user_id)
        if result:
            list_session = ShowSessions()
            list_session.setUserId(user_id)
            sessions = list_session.execute()
            for session in sessions:
                delete_session = DeleteSession()
                delete_session.execute(session['id'])

            list_credentials = ShowCredentials()
            list_credentials.setUserId(user_id)
            credentials = list_credentials.execute()
            for credential in credentials:
                delete_credential = DeleteCredential()
                delete_credential.execute(credential['id'])

            return response_structure(200)
        else:
            return response_structure(500)

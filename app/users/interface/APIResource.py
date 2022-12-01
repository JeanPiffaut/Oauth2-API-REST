from flask_restful import Resource, abort
from flask import request

from app.users.application.CreateUser import CreateUser
from app.users.application.DeleteUser import DeleteUser
from app.users.application.ShowUsers import ShowUsers


class UserResource(Resource):
    def get(self):
        users = ShowUsers()

        if request.args.get('id'):
            users.setFillId(request.args.get('id'))

        if request.args.get('name'):
            users.setFillName(request.args.get('name'))

        if request.args.get('email'):
            users.setFillEmail(request.args.get('email'))

        result = users.execute()
        return result, 200

    def post(self):
        create = CreateUser()

        if request.args.get('name') is None:
            return {'status': 'Error', 'message': 'Bad request'}, 400

        if request.args.get('email') is None:
            return {'status': 'Error', 'message': 'Bad request'}, 400

        create.setName(request.args.get('name'))
        create.setEmail(request.args.get('email'))

        return create.execute(), 201

    def delete(self):
        delete = DeleteUser()

        if request.args.get('id') is None:
            return {'status': 'Error', 'message': 'Bad request'}, 400

        delete.setId(request.args.get('id'))
        result = delete.execute()
        if result:
            return [], 200
        else:
            return [], 500
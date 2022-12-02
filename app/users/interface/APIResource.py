from flask_restful import Resource
from flask import request, abort

import app
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
        return result, 200

    def post(self):
        create = CreateUser()

        if request.args.get('name') is None:
            abort(400)

        if request.args.get('email') is None:
            abort(400)

        create.setName(request.args.get('name'))
        create.setEmail(request.args.get('email'))

        result = create.execute()
        if result:
            return [], 201
        else:
            return [], 500

    def put(self):
        update = UpdateUser()

        if request.args.get('name') is not None:
            update.setName(request.args.get('name'))

        if request.args.get('email') is not None:
            update.setEmail(request.args.get('email'))

        result = update.execute(request.args.get('id'))
        if result:
            return [], 200
        else:
            return [], 500

    def delete(self):
        delete = DeleteUser()

        if request.args.get('id') is None:
            abort(400)

        result = delete.execute(request.args.get('id'))
        if result:
            return [], 200
        else:
            return [], 500

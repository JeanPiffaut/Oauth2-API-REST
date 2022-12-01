from flask_restful import Resource
from flask import request

from app.users.application.show_users import ShowUsers


class UserResource(Resource):
    def get(self):
        users = ShowUsers()

        if request.args.get('id'):
            users.setFillId(request.args.get('id'))

        if request.args.get('name'):
            users.setFillName(request.args.get('name'))

        if request.args.get('email'):
            users.setFillEmail(request.args.get('email'))

        result = users.show()
        return result, 200

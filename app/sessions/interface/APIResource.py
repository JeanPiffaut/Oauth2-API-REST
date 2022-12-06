from flask_restful import Resource
from flask import request, abort

from app import response_structure
from app.sessions.application.CreateSession import CreateSession
from app.sessions.application.ShowSessions import ShowSessions


class SessionResource(Resource):

    def get(self):
        show = ShowSessions()

        if request.args.get('user_id') is not None:
            show.setUserId(request.args.get('user_id'))

        if request.args.get('token') is not None:
            show.setToken(request.args.get('token'))

        if request.args.get('creation_date') is not None:
            show.setCreationDate(request.args.get('creation_date'))

        if request.args.get('last_activity') is not None:
            show.setLastActivity(request.args.get('last_activity'))

        if request.args.get('life_time') is not None:
            show.setLifeTime(request.args.get('life_time'))

        result = show.execute(request.args.get('id'))
        return response_structure(200, result)

    def post(self):
        if request.args.get('user_id') is None:
            abort(400)

        create = CreateSession()
        create.setUserId(request.args.get('user_id'))
        result = create.execute()
        if result:
            return response_structure(201)
        else:
            return response_structure(500)


    def put(self):
        return response_structure(200)

    def delete(self):
        return response_structure(200)

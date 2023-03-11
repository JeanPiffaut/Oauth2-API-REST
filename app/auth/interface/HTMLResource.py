from flask import request, render_template, make_response
from flask_restful import Resource

from app import response_structure


class HTMLResource(Resource):
    def get(self):
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':

            html = render_template('login_template.html')
            response = make_response(html)
            response.headers['Content-Type'] = 'text/html'
            return response
        else:
            return response_structure(200)

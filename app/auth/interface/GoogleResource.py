from flask import url_for, redirect
from flask_restful import Resource

from app.auth_types.application.ShowAuthType import ShowAuthType


class GoogleResource(Resource):
    def get(self):
        auth_types = ShowAuthType()
        auth_types.setName("google")
        result = auth_types.execute()
        auth_type = result[0]

        client_id = auth_type['client_id']
        redirect_uri = "http://127.0.0.1:5000"
        scope = "a"

        url = f"https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=email%20profile&state={scope}"
        return redirect(url)

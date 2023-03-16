from flask import Blueprint

from app import ExtendAPI
from app.auth.interface.APIResource import APIResource
from app.auth.interface.GoogleResource import GoogleResource
from app.auth.interface.HTMLResource import HTMLResource

auth_bp = Blueprint('auth', __name__)
api = ExtendAPI(auth_bp)

# Add endpoints
api.add_resource(HTMLResource, '/', endpoint='auth_resource')
api.add_resource(APIResource, '/v1/login', endpoint='login_resource')
api.add_resource(GoogleResource, '/v1/oauth2/google', endpoint='google_resource')

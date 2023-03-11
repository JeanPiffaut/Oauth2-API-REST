from flask import Blueprint

from app import ExtendAPI
from app.auth.interface.HTMLResource import HTMLResource

auth_bp = Blueprint('auth', __name__)
api = ExtendAPI(auth_bp)

# Add endpoints
api.add_resource(HTMLResource, '/', endpoint='auth_resource')

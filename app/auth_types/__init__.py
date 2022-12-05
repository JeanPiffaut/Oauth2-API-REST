from flask import Blueprint

from app import ExtendAPI
from app.auth_types.interface.APIResource import AuthTypeResource

auth_type_bp = Blueprint('auth_types', __name__)
api = ExtendAPI(auth_type_bp)

# Add endpoints
api.add_resource(AuthTypeResource, '/v1/auth_types', endpoint='auth_type_resource')

from flask import Blueprint

from app import ExtendAPI
from app.sessions.interface.APIResource import SessionResource

sessions_bp = Blueprint('sessions', __name__)
api = ExtendAPI(sessions_bp)

# Add endpoints
api.add_resource(SessionResource, '/v1/sessions', endpoint='session_resource')

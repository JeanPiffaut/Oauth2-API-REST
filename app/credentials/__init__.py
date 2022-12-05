from flask import Blueprint

from app import ExtendAPI
from app.credentials.interface.APIResource import CredentialResource

credentials_bp = Blueprint('credentials', __name__)
api = ExtendAPI(credentials_bp)

# Add endpoints
api.add_resource(CredentialResource, '/v1/credentials', endpoint='credential_resource')

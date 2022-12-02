from flask import Blueprint

from app import ExtendAPI
from app.credentials.interface.APIResource import CredentialResource

credential_bp = Blueprint('credential', __name__)
api = ExtendAPI(credential_bp)

# Add endpoints
api.add_resource(CredentialResource, '/v1/credential', endpoint='credential_resource')
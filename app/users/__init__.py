from flask import Blueprint
from flask_restful import Api

from app import ExtendAPI
from app.users.interface.APIResource import UserResource

users_bp = Blueprint('users', __name__)
api = ExtendAPI(users_bp)

# Add endpoints
api.add_resource(UserResource, '/v1/users', endpoint='user_resource')

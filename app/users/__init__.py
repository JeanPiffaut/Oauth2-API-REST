from flask import Blueprint
from flask_restful import Api

users_bp = Blueprint('users', __name__)
api = Api(users_bp)

# Add endpoints
# api.add_resource(UserResource, '/v1/users', endpoint='user_resource')

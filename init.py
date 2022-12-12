import os

from flask import Flask
from flask_restful import Api

from app.auth_types import auth_type_bp
from app.credentials import credentials_bp
from app.sessions import sessions_bp
from app.users import users_bp

setting_module = os.getenv('APP_SETTINGS_MODULE')

api = Flask(__name__)

if __name__ == "__main__":
    api.config.from_object(setting_module)
    Api(api, catch_all_404s=True)
    api.url_map.strict_slashes = False

    api.register_blueprint(users_bp)
    api.register_blueprint(auth_type_bp)
    api.register_blueprint(credentials_bp)
    api.register_blueprint(sessions_bp)

    api.run(debug=True)

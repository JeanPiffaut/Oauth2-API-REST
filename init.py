import os

from flask import Flask
from flask_restful import Api

from app.auth import auth_bp
from app.users import users_bp

setting_module = os.getenv('APP_SETTINGS_MODULE')

api = Flask(__name__, template_folder='templates')

if __name__ == "__main__":
    api.config.from_object(setting_module)
    Api(api, catch_all_404s=True)
    api.url_map.strict_slashes = False

    api.register_blueprint(auth_bp)
    api.register_blueprint(users_bp)

    api.run(debug=True)

import os

from flask import Flask
from flask_restful import Api

from app import register_error_handlers
from app.users import users_bp

setting_module = os.getenv('APP_SETTINGS_MODULE')

app = Flask(__name__)

if __name__ == "__main__":
    app.config.from_object(setting_module)
    Api(app, catch_all_404s=True)
    app.url_map.strict_slashes = False

    app.register_blueprint(users_bp)

    register_error_handlers(app)

    app.run(debug=True)

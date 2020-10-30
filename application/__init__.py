import os

from flask import Flask
from config import config_by_name


def create_app(config_name):
    # Configure flask app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_by_name[config_name])

    # Configure blueprints
    from application.routes import api_routes
    app.register_blueprint(api_routes.bp)

    return app

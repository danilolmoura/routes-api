import os

def create_app(config_name):
    from flask import Flask
    from config import config_by_name

    # Configure flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])

    # Configure blueprints
    from application.route import api_routes
    app.register_blueprint(api_routes.bp, url_prefix='/route')

    # Define main route
    @app.route('/')
    def index():
        return '<a href="https://github.com/danilolmoura/routes-api#routes-api">Read the docs!</a>'

    return app

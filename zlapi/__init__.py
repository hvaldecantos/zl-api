from flask import Flask
from flask_jwt_extended import JWTManager
import os
from .auth import ZlapiBaseException


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True, static_folder=None)
    app.config.from_object('config')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    JWTManager(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .database import db
    db.init_app(app)

    # nested blueprint to configure the api
    from flask import Blueprint
    api = Blueprint('api', __name__, url_prefix = '/api')

    @api.get("/")
    def initial_endpoint():
        return {"message": "Initial api structure deployed."}

    from . import auth
    api.register_blueprint(auth.bp)

    app.register_blueprint(api)

    # error handling
    @app.errorhandler(404)
    def page_not_found(e):
        return {'error': 'Resource not found.'}, 404

    @app.errorhandler(ZlapiBaseException)
    def intercept_zlapi_base_exceptions(e):
        return {'error': e.description}, e.code

    return app

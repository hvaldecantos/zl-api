from flask import Flask
import os

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True, static_folder=None)
    app.config.from_object('config')
    app.config.from_pyfile('config.py', silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # nested blueprint to configure the api
    from flask import Blueprint
    api = Blueprint('api', __name__, url_prefix = '/api')

    @api.get("/")
    def initial_endpoint():
        return {"message": "Initial api structure deployed."}

    app.register_blueprint(api)

    return app

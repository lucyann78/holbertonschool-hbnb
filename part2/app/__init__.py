from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
# Import other namespaces as needed

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register user namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    # Register other namespaces here

    return app

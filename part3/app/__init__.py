from flask import Flask
from flask_restx import Api
from config import Config
from app.models import db  # Importar SQLAlchemy
from flask_jwt_extended import JWTManager

# Importar los namespaces de Flask-RESTx
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)  # Cargar configuración

    # Inicializar SQLAlchemy y JWT
    db.init_app(app)
    JWTManager(app)

    # Inicializar Flask-RESTx API
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Registrar namespaces en la API
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')

    return app

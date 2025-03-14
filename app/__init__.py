# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config  # Cambiar DevelopmentConfig por Config

# Instanciar extensiones
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    """Crear y configurar la aplicación Flask."""
    app = Flask(__name__)

    # Cargar configuración desde Config
    app.config.from_object(config_class)

    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Importar y registrar blueprints
    from app.api.v1.users import users_bp
    from app.api.v1.places import places_bp
    from app.api.v1.auth import auth_bp

    app.register_blueprint(users_bp, url_prefix="/api/v1/users")
    app.register_blueprint(places_bp, url_prefix="/api/v1/places")
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")

    return app


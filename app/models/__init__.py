from flask_sqlalchemy import SQLAlchemy

# Inicializar SQLAlchemy
db = SQLAlchemy()

# Importar modelos para que SQLAlchemy los registre
from .user import User
from .place import Place
from .review import Review  # Asegúrate de que review.py existe en models

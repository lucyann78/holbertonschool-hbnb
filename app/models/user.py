# app/models/user.py

from app import db  # Importar solo db aquí

class User(db.Model):
    __tablename__ = "user"  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relación con Review
    reviews = db.relationship("Review", backref="user", cascade="all, delete-orphan", lazy=True)


    def set_password(self, password):
        """Hashea la contraseña y la guarda en password_hash."""
        from app import bcrypt  # Importar aquí para evitar import circular
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Verifica si la contraseña es correcta."""
        from app import bcrypt  # Importar aquí también
        return bcrypt.check_password_hash(self.password_hash, password)

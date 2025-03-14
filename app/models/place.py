from app.models import db  # Importar la base de datos

class Place(db.Model):
    __tablename__ = "place"  # Asegurar coherencia con los ForeignKey en review.py

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(255), nullable=False)

    # Relación con Review
    reviews = db.relationship("Review", back_populates="place", cascade="all, delete-orphan")

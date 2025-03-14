from app.models import db  # Importar la base de datos
from datetime import datetime

class Review(db.Model):
    __tablename__ = "review"  # Asegurar que el nombre sea coherente con los ForeignKey

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # Relación con User
    place_id = db.Column(db.Integer, db.ForeignKey("place.id"), nullable=False)  # Relación con Place
    rating = db.Column(db.Integer, nullable=False)  # Calificación del 1 al 5
    comment = db.Column(db.Text, nullable=False)  # Texto de la reseña
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de creación
    # Relación con User
    user = db.relationship("User")
  
    place = db.relationship("Place", back_populates="reviews")  # Relación con Place

    def __repr__(self):
        return f"<Review {self.id} - {self.rating} stars>"

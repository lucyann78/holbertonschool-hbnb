from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify
from app.models import Place  # Asegúrate de importar tu modelo de Place

places_bp = Blueprint("places", __name__)

@places_bp.route("/edit/<int:place_id>", methods=["PUT"])
@jwt_required()  # Requiere autenticación
def edit_place(place_id):
    user_id = get_jwt_identity()  # Obtener el ID del usuario desde el JWT
    place = Place.query.get_or_404(place_id)

    if place.owner_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403  # Solo el propietario puede editar

    # Lógica para editar el lugar
    return jsonify({"message": "Place updated"}), 200

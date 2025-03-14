from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import User, db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get("email")).first()

    if user and user.check_password(data["password"]):
        # Crear el token JWT
        token = create_access_token(identity=user.id)
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

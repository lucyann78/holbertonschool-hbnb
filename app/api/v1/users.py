from flask import Blueprint, request, jsonify
from app.models import db, User

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["POST"])
def register_user():
    data = request.get_json()
    
    email = data.get("email")
    password = data.get("password")
    
    # Validación básica
    if not email or not password:
        return jsonify({"error": "Email y contraseña son requeridos."}), 400

    # Validar formato básico del email (opcional)
    if "@" not in email:
        return jsonify({"error": "Email inválido."}), 400

    # Validar la contraseña (mínimo 8 caracteres)
    if len(password) < 8:
        return jsonify({"error": "La contraseña debe tener al menos 8 caracteres."}), 400

    # Verificar si el email ya está registrado
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "El email ya está registrado."}), 400

    # Crear el usuario y hashear la contraseña
    user = User(email=email)
    user.set_password(password)  # Guardar hash de la contraseña

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error al registrar el usuario: {e}"}), 500

    return jsonify({
        "id": user.id,
        "message": "Usuario creado exitosamente."
    }), 201


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)  # Obtener usuario o 404 si no existe

    # Retornar datos del usuario sin la contraseña
    return jsonify({
        "id": user.id,
        "email": user.email,
        "is_admin": user.is_admin
    }), 200

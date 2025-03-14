from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.models import db, User  # Importa el modelo User de la base de datos

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password for the user account')  # Añadir password al modelo
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Verificar si el correo ya está registrado
        existing_user = User.query.filter_by(email=user_data['email']).first()
        if existing_user:
            return {'error': 'Email already registered'}, 400

        # Crear el nuevo usuario
        new_user = User(email=user_data['email'], first_name=user_data['first_name'], last_name=user_data['last_name'])
        new_user.set_password(user_data['password'])  # Usar el método set_password para guardar la contraseña cifrada

        db.session.add(new_user)
        db.session.commit()

        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

# app/api/v1/__init__.py
from flask_restful import Resource
from flask_restx import Api, Namespace
from flask import request

api = Api()
amenities_api = Namespace('amenities', description='Amenities related operations')

@api.route('/api/v1/')
class ApiV1Index(Resource):
    def get(self):
        return {"message": "API v1 is working!"}

# Add the amenities namespace
api.add_namespace(amenities_api, path='/api/v1/amenities')

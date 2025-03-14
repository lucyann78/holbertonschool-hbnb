from flask_restx import Api
from .v1.places import api as places_api

api = Api()
api.add_namespace(places_api, path='/api/v1/places')
from flask_restx import Api
from app.api.v1.reviews import api as reviews_api

api = Api()
api.add_namespace(reviews_api)

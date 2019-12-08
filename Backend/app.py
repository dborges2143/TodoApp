from flask import Blueprint
from flask_restful import Api
# from resources.User import User
from resources.Register import Register

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
# api.add_resource(User, '/user')
api.add_resource(Register, '/register')
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Namespace, Resource, fields


api = Namespace('protected', description='Protection operations')


@api.route('')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        current_user = get_jwt_identity() # Retrieve the user's identity from the token
        return {'message': f'Hello, user {current_user["id"]}'}, 200

from typing import Optional
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.services import facade

api = Namespace("auth", description="Authentication routes")

login_model = api.model('Login', {
    'email': fields.String(description='Login Email'),
    'password': fields.String(description='Login password')
})

@api.route("/login")
class Login(Resource):
    @api.expect(login_model)
    @api.response(401, "Invalid Credentials")
    @api.response(400, "Bad Request")
    @api.response(500, "Server Error")
    def post(self):
        """Authenticate a user using basic credential auth"""
        try:
            credentials = api.payload
            email: str = credentials.get("email", None)
            password: str = credentials.get("password", None)
            if not email or not password:
                return {"error":"Bad Request"}, 400
            user: Optional[User] = facade.get_user_by_email(email=email)
            if not user or not user.verify_password(password=password):
                return {"error": "Unauthorized"}, 401
            additional_claims = {
               'is_admin': user.is_admin
            }
            return {
                "access_token": create_access_token(identity=user.id, additional_claims=additional_claims)
            }, 200
        except Exception as ex:
            return {"error": "Server Error"}, 500
        
@api.route("/me")
class Me(Resource):
    @jwt_required()
    @api.response(401, "Not Authorized")
    @api.response(404, "Not Found")
    @api.response(500, "Server error")
    def get(self):
        """Return authenticate user info"""
        try:
           sub = get_jwt_identity()
           user: Optional[User] = facade.get_user(sub)
           if not user:
               return {"error": "User not found"}, 404
           else:
               return user.to_dict(excluded_attr=["password"]), 200
        except Exception as ex:
            return {"error": "Server Error"}, 500
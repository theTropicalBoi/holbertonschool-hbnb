from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import config

# Initialize Flask app
jwt = JWTManager()
bcrypt = Bcrypt()

def createApp(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version="1.0", title="HBnB API", description="HBnB Application API", doc="/api/v1")

    bcrypt.init_app(app)
    jwt.init_app(app)
    
    return app

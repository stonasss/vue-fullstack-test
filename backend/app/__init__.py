from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .utils.database import init_db

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config.from_object('config.Config')
    init_db(app)
    app.config['JWT_SECRET_KEY']
    JWTManager(app)
    from .routes.game_routes import game_routes
    from .routes.auth_routes import auth_routes
    app.register_blueprint(game_routes)
    app.register_blueprint(auth_routes)

    return app
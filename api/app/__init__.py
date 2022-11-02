from datetime import timedelta
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from flask_sock import Sock
from flask_seeder import FlaskSeeder

mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
# create jwt manager 
jwt = JWTManager()
socketio = SocketIO()
websock = Sock()
seeder = FlaskSeeder()



def create_app():
    """
        app factory function.
        return the configured app object
    """

    app = Flask(__name__)

    # configuration
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')


    ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_TOKEN_EXPIRES
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = REFRESH_TOKEN_EXPIRES

    # register blueprints
    register_blueprints(app)

    # intialize extensions
    initialize_extensions(app)

    return app    

def register_blueprints(app):
    from app.users import users_bp
    from app.products import products_bp
    from app.orders import orders_bp
    from app.reorders import reorders_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(reorders_bp)


def initialize_extensions(app):
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    jwt.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    websock.init_app(app)
    seeder.init_app(app, db)


@jwt.user_identity_loader
def user_identity_lookup(user):

    return user

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    from app.users.models import User
    identity = jwt_data["sub"]
    user_id = identity['_id']
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return None
    
    return user
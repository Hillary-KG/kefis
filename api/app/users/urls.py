from flask_jwt_extended import jwt_required
from . import users_bp
from .views import UserView


@users_bp.route('/register', methods=["POST"])
# @jwt_required()
def register_user():
    """route to register user"""
    return UserView().add_user()

@users_bp.route('/login', methods=["POST"])
def login():
    """route to login user"""
    return UserView().login()

@users_bp.route('/edit-user', methods=["PUT"])
@jwt_required()
def update():
    """route to edit user details"""
    return UserView().update_user()
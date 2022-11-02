

from datetime import datetime, timedelta
from pytz import timezone

from flask import request, jsonify
from flask_jwt_extended import current_user

from app import db
from .models import User
from app.helpers.password_helper import hash_password, unhash_password
from app.helpers.jwt import sign_token

TZ = timezone('Africa/Nairobi')
class UserView:
    """holds auth view logic"""
    def add_user(self):
        """view func() to create a new user"""
        try:
            request_data = request.get_json(force=True)
            if not request_data:
                return jsonify({
                    'success': False,
                    'msg': "Bad request! No data submitted"
                }), 400
            request_data['password'] = hash_password(str(request_data['password']).encode())
            user_id = User().create(request_data)

            if not user_id:
                return jsonify({
                    'success': False,
                    'msg': "could not create user! Try again" 
                }), 400
            
            return jsonify({
                    'success': True,
                    'msg': "user created successfully!"
                }), 201
        except Exception as e:
            # log exception
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500

    def login(self):
        '''view func() to login user'''
        try:
            request_data = request.get_json(force=True)
            if not request_data:
                message = {
                    'status': 400,
                    'description': "no data submitted required!"
                }
                return jsonify(message), 400
            email = request_data['email']
            password = request_data['password']
            user = User.query.filter_by(email=email).first()

            
            if not user:
                message = {
                    'status': 401,
                    'description': "Invalid username. User does not exist"
                }
                return jsonify(message), 401
            
            if not unhash_password(password.encode(), user.password.encode()):
                message = {
                    'status': 401,
                    'description': "Unauthorized! Invalid username or password!."
                }
                return jsonify(message), 401
            
            jwt_payload = {
                'user_id': user.id,
            }
            
            access_token, refresh_token = sign_token(jwt_payload)
            last_login = datetime.now(tz=TZ).strftime("%Y-%m-%d %H:%M:%S")
            user.last_login = last_login
            db.session.add(user)
            db.session.commit()


            return jsonify({
                'msg': "login successful",
                'user_type': user.user_type,
                'access': {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            }), 200

        except Exception as error:
            message = {'status': 500,
                       'description': 'An exception occured. Error description ' + format(error)}
            return jsonify(message), 500
    
    def update_user(self):
        """view func() to update user"""
        try:
            if not current_user:
                return jsonify({
                    'success': False,
                    'msg': "Unauthorized"
                }), 401
            
            update_data = request.get_json(force=True)
            if not update_data:
                return jsonify({
                    'success': False,
                    'msg': "no update data submitted"
                }), 400

            if update_data.get('password'):
                update_data['password'] = hash_password(str(update_data['password']).encode())

            user_id = current_user.id

            updated_ = User().update_user(user_id, update_data)
            if not updated_:
                return jsonify({
                    'success': False,
                    'msg': "failed. could not update user",
                }), 400
                
            return jsonify({
                'success': True,
                'msg': "user updated successfully"
            }), 200
        except Exception as e:
            # log exception 
            return jsonify({
                'success': False,
                'msg': f"An Exception occured: {str(e)}",
            }), 500
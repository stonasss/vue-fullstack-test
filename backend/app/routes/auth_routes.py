from flask import Blueprint, jsonify, request, current_app
from ..services.auth_service import AuthService
from ..utils.auth_utils import create_jwt_token

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'status': 'error', 'message': 'Username and password are required'}), 400

    db = current_app.db
    auth_service = AuthService(db)
    try:
        user_id = auth_service.register_user(username, password)
        return jsonify({
            'status': 'success',
            'message': 'User registered successfully',
            'user_id': user_id
        }), 201
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'status': 'error', 'message': 'Username and password are required'}), 400

    db = current_app.db
    auth_service = AuthService(db)
    try:
        user = auth_service.login_user(username, password)
        token = create_jwt_token(str(user['_id']))
        return jsonify({
            'status': 'success',
            'message': 'Login successful',
            'token': token
        }), 200
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 401
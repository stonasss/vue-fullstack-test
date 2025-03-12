from flask import Blueprint, jsonify, request, current_app
from app.services.game_service import GameService
from app.middleware.auth_middleware import auth_required

game_routes = Blueprint('game_routes', __name__)

@game_routes.route('/games', methods=['GET', 'POST'])
@auth_required
def handle_games(current_user_id):
    db = current_app.db
    service = GameService(db)

    if request.method == 'POST':
        new_game = request.json
        game_id = service.add_game(new_game)
        return jsonify({
            'status': 'success',
            'message': 'Game added successfully!',
            'game_id': game_id
        }), 201

    games = service.get_all_games()
    return jsonify({
        'status': 'success',
        'games': games
    }), 200

@game_routes.route('/games/<id>', methods=['PUT'])
@auth_required
def update_game(current_user_id, id):
    db = current_app.db
    service = GameService(db)
    updated_game = request.json
    service.update_game(id, updated_game)
    return jsonify({
        'status': 'success',
        'message': 'Game updated successfully!'
    }), 200

@game_routes.route('/games/<id>', methods=['DELETE'])
@auth_required
def delete_game(current_user_id, id):
    db = current_app.db
    service = GameService(db)
    service.delete_game(id)
    return jsonify({
        'status': 'success',
        'message': 'Game deleted successfully!'
    }), 200
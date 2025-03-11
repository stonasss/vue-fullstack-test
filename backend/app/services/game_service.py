from bson.objectid import ObjectId
from ..exceptions.custom_exceptions import GameNotFoundError

class GameService:
    def __init__(self, db):
        self.games = db.games

    def get_all_games(self):
        games = list(self.games.find())
        for game in games:
            game['_id'] = str(game['_id'])
        return games

    def add_game(self, game_data):
        result = self.games.insert_one(game_data)
        return str(result.inserted_id)

    def update_game(self, game_id, game_data):
        game_data.pop('_id', None)
        result = self.games.update_one({'_id': ObjectId(game_id)}, {'$set': game_data})
        if result.matched_count == 0:
            raise GameNotFoundError(f"Game with ID {game_id} not found.")

    def delete_game(self, game_id):
        result = self.games.delete_one({'_id': ObjectId(game_id)})
        if result.deleted_count == 0:
            raise GameNotFoundError(f"Game with ID {game_id} not found.")
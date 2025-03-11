from bson.objectid import ObjectId
from ..utils.auth_utils import hash_password

class UserModel:
    def __init__(self, db):
        self.users = db.users

    def create_user(self, username, password):
        if self.users.find_one({'username': username}):
            raise ValueError('Username already exists')

        hashed_password = hash_password(password)

        user = {
            'username': username,
            'password': hashed_password
        }
        result = self.users.insert_one(user)
        return str(result.inserted_id)

    def find_user_by_username(self, username):
        return self.users.find_one({'username': username})
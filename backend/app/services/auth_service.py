from ..models.user_model import UserModel
from ..utils.auth_utils import hash_password, verify_password

class AuthService:
    def __init__(self, db):
        self.user_model = UserModel(db)

    def register_user(self, username, password):
        if self.user_model.find_user_by_username(username):
            raise ValueError('Username already exists')

        hashed_password = hash_password(password)

        user = {
            'username': username,
            'password': hashed_password
        }
        result = self.user_model.users.insert_one(user)
        return str(result.inserted_id)

    def login_user(self, username, password):
        user = self.user_model.find_user_by_username(username)
        if not user or not verify_password(password, user['password']):
            raise ValueError('Invalid username or password')

        return user
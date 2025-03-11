from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps

def auth_required(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        kwargs['current_user_id'] = current_user_id
        return f(*args, **kwargs)
    return decorated_function
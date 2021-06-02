from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from .database.models import User
import datetime

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.post('/signup')
def signup():
    body = request.get_json()
    user = User(**body)
    user.hash_password()
    user.save()
    id = user.id
    return {'id': str(id)}, 200

@bp.post('/login')
def login():
    body = request.get_json()
    user = User.objects.get(email=body.get('email'))
    authorized = user.check_password(body.get('password'))
    if not user or not authorized:
        return {'error': 'Invalid email or password'}, 401

    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=str(user.id), expires_delta=expires)
    return {'token': access_token}, 200

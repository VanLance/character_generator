from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token

from schemas import AuthUserSchema, UserSchema, UserSchemaNested
from . import bp
from models import UserModel

@bp.post('/register')
@bp.arguments(UserSchemaNested)
@bp.response(201, UserSchemaNested)
def register(user_data):
  user = UserModel()
  user.from_dict( user_data)
  try:
    user.save()
    print(user, user.characters.all(), 'user ===================')
    return user 
  except IntegrityError:
    abort(400, message='Username or Email already Taken')

@bp.post('/login')
@bp.response(200, UserSchemaNested)
@bp.arguments(AuthUserSchema)
def login(login_info):
  if 'username' not in login_info and 'email' not in login_info:
    abort(400, message='Please include Username or Email!')
  if 'username' in login_info:
    user = UserModel.query.filter_by(username=login_info['username']).first()
  else:
    user = UserModel.query.filter_by(email=login_info['email']).first()
  if user and user.check_password(login_info['password']):
    user.access_token = create_access_token(identity=user.id)
    return user 
  abort(400, message='Invalid Username Or Password')
  

from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import abort
from . import bp

from schemas import UserSchema, UserSchemaNested
from models import UserModel
# user routes

@bp.route('/user/<user_id>')
class User(MethodView):

  @bp.response(200, UserSchemaNested)
  def get(self, user_id):
    user = None
    print(user_id)
    if user_id.isdigit():
      user = UserModel.query.get(user_id)
    if not user:
      user = UserModel.query.filter_by(username = user_id).first()
      print(user)
    if user:
      return user
    else:
      abort(400, message='User not found')

  @jwt_required()  
  @bp.arguments(UserSchema)
  def put(self, user_data, user_id):
    user = UserModel.query.get(get_jwt_identity())
    if user and user.id == user_id:
      user.from_dict(user_data)
      user.commit()
      return { 'message': f'{user.username} updated'}, 202
    abort(400, message = "Invalid User")

  @jwt_required()
  def delete(self, user_id):
    user = UserModel.query.get(get_jwt_identity())
    if user == user_id:
      user.delete()
      return { 'message': f'User: {user.username} Deleted' }, 202
    return {'message': "Invalid username"}, 400

@bp.route('/user')
class UserList(MethodView):

  @bp.response(200, UserSchema(many = True))
  def get(self):
   return UserModel.query.all()
  

@bp.route('/user/follow/<followed_id>')
class FollowUser(MethodView):

  @jwt_required()
  def post(self, followed_id):
    followed = UserModel.query.get(followed_id)
    follower =UserModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.follow(followed)
      followed.commit()
      return {'message':'user followed'}
    else:
      return {'message':'invalid user'}, 400
  @jwt_required()  
  def put(self, followed_id):
    followed = UserModel.query.get(followed_id)
    follower = UserModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.unfollow(followed)
      followed.commit()
      return {'message':'user unfollowed'}
    else:
      return {'message':'invalid user'}, 400
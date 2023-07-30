from flask import  request, jsonify, make_response
from . import api
from werkzeug.wrappers import response
from char_inventory.helpers import token_required
from char_inventory.models import  User, user_schema
from werkzeug.security import check_password_hash

@api.route('/getdata')
@token_required
def get_data(current_user_token):
    return { 'some' : 'value' }

# USER LOGIN
@api.post('/login')
def api_login():
    [username,password] = [request.json['username'], request.json['password']]
    print(username,password)
    user = User.query.filter_by(username = username).first()
    # print(user,user.password, check_password_hash(user.password, password))
    if not user or not check_password_hash(user.password, password):
        return make_response(jsonify({'message' : 'Username or Passord Invalid'}),404)
    return jsonify(user_schema.dump(user))

@api.post('register')
def api_register():
    try:
        [username,email,password] = [request.json['username'], request.json['email'], request.json['password']]
        print(username,email,password)
        u = User(username=username, email=email, password=password)
        print(u)
        u.commit()
        return make_response(jsonify({
            'message':f'{u.username} Registered',
            'token':u.token                              
        }))
    except:
        return make_response(jsonify({'message' : 'Username or Email already Taken'}),404)
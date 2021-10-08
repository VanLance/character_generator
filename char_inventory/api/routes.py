import re
from flask import Blueprint, json, request, jsonify
from werkzeug.wrappers import response
from char_inventory.helpers import token_required
from char_inventory.models import db, User, Character, character_schema, characters_schema


api = Blueprint('api', __name__,url_prefix = '/api')

@api.route('/getdata')
@token_required
def get_data(current_user_token):
    return { 'some' : 'value' }

# CREATE CHARACTER ENDPOINT
@api.route('/characters', methods = ['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    level = request.json['level']
    race = request.json['race']
    charClass = request.json['charClass']
    hp = request.json['hp']
    ac = request.json['ac']
    strength = request.json['strength']
    dexterity= request.json['dexterity']
    constitution = request.json['constitution']
    intellegence = request.json['intellegence']
    wisdom = request.json['wisdom']
    charisma= request.json['charisma']
    spellDC= request.json['spellDC']
    user_token = current_user_token.token

    character = Character(name,level,race,charClass,hp,ac,strength,dexterity,constitution,intellegence, wisdom, charisma, spellDC, user_token)
    db.session.add(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)

# RETRIEVE ALL CHARACTERS ENDPOINT
@api.route('/characters',methods = ['GET'])
@token_required
def get_characters(current_user_token):
    owner = current_user_token.token
    characters = Character.query.filter_by(user_token = owner).all()
    response = characters_schema.dump(characters)
    return jsonify(response)


# RETRIEVE ONE CHARACTER ENDPOINT
@api.route('/characters/<id>', methods = ['GET'])
@token_required
def get_character(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        character = Character.query.get(id)
        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({'message' : 'Valid Token Required'}),401

#UPDATE CHARACTER ENDPOINT
@api.route('/characters/<id>', methods = ['Post', 'PUT'])
@token_required
def update_character(current_user_token, id):
    character = Character.query.get(id) # Get Character Instance
    character.name = request.json['name']
    character.level = request.json['level']
    character.race = request.json['race']
    character.charClass = request.json['charClass']
    character.hp = request.json['hp']
    character.ac = request.json['ac']
    character.strength = request.json['strength']
    character.dexterity= request.json['dexterity']
    character.constitution = request.json['constitution']
    character.intellegence = request.json['intellegence']
    character.wisdom = request.json['wisdom']
    character.charisma= request.json['charisma']
    character.spellDC= request.json['spellDC']
    character.user_token = current_user_token.token

    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)

# DELETE CHARACTER ENDPOINT
@api.route('/characters/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)
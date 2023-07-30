from flask import  json, request, jsonify, make_response
from . import api
from char_inventory.helpers import token_required
from char_inventory.models import db, Character, character_schema, characters_schema,user_schema
from char_inventory.buildCharacter.browserCode import createCharacter, runCreate


# CREATE CHARACTER ENDPOINT
@api.post('/create')
@token_required
def create_character(current_user_token):
    print(request.json,'json')
    try:
        name = request.json['name']
        level = int(request.json['level'])
        race = request.json['race']
        _class = request.json['characterClass']
        gender = request.json['gender']
        newCharacter = createCharacter(name, gender, race, _class, level)
        runCreate(newCharacter)
        commitCharacter=Character(newCharacter.name.title(), newCharacter.level, newCharacter.race, newCharacter.gender, newCharacter._class, newCharacter.hp, newCharacter.ac, newCharacter.stats['str'],
            newCharacter.stats['dex'],newCharacter.stats['con'],newCharacter.stats['int'],newCharacter.stats['wis'],
            newCharacter.stats['cha'], newCharacter.dc, current_user_token.token)
        print('\n\nADDING=================================\n\n')
        db.session.add(commitCharacter)
        db.session.commit()
        print(commitCharacter,commitCharacter.strength)

        response = character_schema.dump(commitCharacter)
        print(response,'=====response')
        return jsonify(response) # will be response
    except:
        return make_response({'message':'Please enter valid form data'},404)
    
# RETRIEVE ALL CHARACTERS FOR SINGLE USER ENDPOINT
@api.get('/characters')
@token_required
def get_characters(current_user_token):
    print(current_user_token)
    ownerToken = current_user_token.token
    characters = Character.query.filter_by(user_token = ownerToken).all()
    print([c for c in characters])
    response = characters_schema.dump(characters)[::-1]
    return jsonify(response)

# RETRIEVE ALL CHARACTERS ENDPOINT
@api.get('/universe')
def all_characters():
    characters = Character.query.all()
    print(characters)
    response = characters_schema.dump(characters)
    return jsonify(response)

# RETRIEVE ONE CHARACTER ENDPOINT
@api.route('/character/<id>', methods = ['GET'])
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
@api.put('/update/<id>')
@token_required
def update_character(current_user_token, id):
    character = Character.query.get(id) # Get Character Instance
    character.name = request.json['name']
    character.level = request.json['level']
    character.race = request.json['race']
    character._class = request.json['_class']
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
@api.delete('/delete/<id>')
@token_required
def delete_character(current_user_id,id):
    character = Character.query.get(id)
    if not character:
        return make_response({'message':"character doesn't exist"},404)
    print(character,'char')
    print()
    current_user_token= request.headers['x-access-token']
    if current_user_token==character.user_token:
        characterName = character.name
        db.session.delete(character)
        db.session.commit()
        return jsonify(200, {'message':f'{characterName} Deleted'})
    else:
        return make_response({'message':"you must own character"}, 401)
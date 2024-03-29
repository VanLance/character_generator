from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity

from character_creation.index import createCharacter, runCreate
from models import CharacterStatsModel, CharacterModel, UserModel
from . import bp
from schemas import CharacterAuthSchema, CharacterNestedSchema, CharacterSchema

@bp.route('/character')
class CharacterList(MethodView):

    @jwt_required()
    @bp.arguments(CharacterSchema)
    @bp.response(201, CharacterNestedSchema)
    def post(self, character_data):

        print(character_data)
        character = createCharacter(**character_data)
        
        
        character_stats = CharacterStatsModel()
        character_stats.from_dict(runCreate(character))

        character_model = CharacterModel()
        character_model.from_dict(character_data)
        
        character_stats.save()

        character_model.user_id = get_jwt_identity()
        character_model.stats_id = character_stats.id
        character_model.save()

        return character_model
        
        abort(400, message='Failed')

    @bp.response(200, CharacterNestedSchema(many=True))
    def get(self):
        return CharacterModel.query.all()

@bp.route('/character/<character_id>')
class Character(MethodView):

    @bp.response(200, CharacterNestedSchema)
    def get(self, character_id):
        character = CharacterModel.query.get(character_id)
        if character:
            return character
        abort(message='Invalid Character')

    @bp.arguments(CharacterAuthSchema)
    @bp.response(201, CharacterSchema)
    def put(self, character_and_user_data, character_id):
        pass
        
    @jwt_required()
    def delete(self, character_id):
        character = CharacterModel.query.get(character_id)
        print(character, character_id, 'character =======================')
        if not character:
            abort(message="Invalid Character")
        if character.user_id != get_jwt_identity():
            abort(message="No Access")
        character.delete()        
        return  { 'message': f'{character_id} deleted'}
from flask.views import MethodView

from . import bp

from models import CharacterModel
from schemas import AuthUserSchema, CharacterAuthSchema, CharacterNestedSchema, CharacterSchema

@bp.route('/character')
class CharacterList(MethodView):

    @bp.arguments(CharacterSchema)
    @bp.response(201, CharacterSchema)
    def post(self, character_data):
        pass

    @bp.response(200, CharacterSchema(many=True))
    def get(self):
        pass

@bp.route('/character/<character_id>')
class Character(MethodView):

    @bp.response(200, CharacterNestedSchema)
    def get(self):
        pass
    
    @bp.arguments(CharacterAuthSchema)
    @bp.response(201, CharacterSchema)
    def put(self, character_and_user_data):
        pass

    @bp.arguments(CharacterAuthSchema)
    def delete(self, character_and_user_data):
        pass
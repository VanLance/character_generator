from marshmallow import Schema, fields

class UserSchema(Schema):
	id = fields.Str(dump_only = True)
	access_token = fields.Str(dump_only = True)
	username = fields.Str(required = True)
	email = fields.Str(required = True)
	password = fields.Str(required = True, load_only = True)
	first_name = fields.Str()
	last_name = fields.Str()

class StatsSchema(Schema):
	hp = fields.Integer()	
	ac = fields.Integer()	
	strength = fields.Integer()	
	dexterity = fields.Integer()	
	constitution = fields.Integer()	
	intelligence = fields.Integer()	
	wisdom= fields.Integer()	
	charisma = fields.Integer()
	spellDC = fields.Integer()

class CharacterSchema(Schema):
	id = fields.Str(dump_only= True)
	name = fields.Str(required = True)
	level = fields.Str(required = True)
	race = fields.Str(required = True)
	gender = fields.Str(required = True)
	_class = fields.Str(required = True)
	stats = fields.Nested(StatsSchema, dump_only = True)

class UserSchemaNested(UserSchema):
	characters = fields.List(fields.Nested(CharacterSchema), dump_only=True)
	followed = fields.List(fields.Nested(UserSchema), dump_only=True)

class CharacterNestedSchema(CharacterSchema):
	user = fields.Nested(UserSchema)

class UpdateUserSchema(Schema):
	username = fields.Str()
	email = fields.Str()
	password = fields.Str(required = True, load_only = True)
	new_password = fields.Str()
	first_name = fields.Str()
	last_name = fields.Str()

class AuthUserSchema(Schema):
	username = fields.Str()
	email = fields.Str()
	password = fields.Str(required = True, load_only = True)

class CharacterAuthSchema(CharacterSchema, AuthUserSchema):
  	pass
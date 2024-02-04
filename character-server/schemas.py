from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  username = fields.Str(required = True)
  email = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True)
  first_name = fields.Str()
  last_name = fields.Str()

class CharacterSchema(Schema):
  pass
  
class UserSchemaNested(UserSchema):
  characters = fields.List(fields.Nested(CharacterSchema), dump_only=True)
  followed = fields.List(fields.Nested(UserSchema), dump_only=True)

class CharacterNestedSchema(CharacterSchema):
  pass

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

class CharacterAuthSchema(CharacterSchema, UserSchema):
  pass
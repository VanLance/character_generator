from flask_login.login_manager import LoginManager
from flask_sqlalchemy import SQLAlchemy
import uuid 
from datetime import datetime


# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Import Secrets
import secrets

#Imports for Login Manager
from flask_login import UserMixin

# Imports for Flask Login
from flask_login import LoginManager

# Immports Marsh..
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.String(150), primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default='')
    username = db.Column(db.String(150), unique= True, nullable = False)
    email = db.Column(db.String(150), unique= True, nullable = False)
    password = db.Column(db.String, nullable=True, default = '')
    token = db.Column(db.String, default= '', unique = True)
    date_created =  db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    character = db.relationship('Character', backref = 'owner', lazy = True)

    def __init__(self, email,username, first_name= '', last_name= '', id = '', password= '', token = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name= last_name
        self.username = username
        self.password = self.set_password(password)
        self.email= email
        self.token = self.set_token(24)
        
        
    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User Email: {self.email} User ID: {self.id}.'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class Character(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(100))
    level = db.Column(db.Numeric(precision = 2))
    race = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    _class = db.Column(db.String(150))
    hp = db.Column(db.Numeric(precision = 3))
    ac = db.Column(db.Numeric(precision = 2))
    strength = db.Column(db.Numeric(precision = 2))
    dexterity = db.Column(db.Numeric(precision = 2))
    constitution = db.Column(db.Numeric(precision = 2))
    intellegence = db.Column(db.Numeric(precision = 2))
    wisdom = db.Column(db.Numeric(precision = 2))
    charisma = db.Column(db.Numeric(precision = 2))
    spellDC = db.Column(db.Numeric(precision = 2), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, level, race, gender, _class, hp, ac, strength, dexterity, constitution, intellegence, wisdom, charisma, spellDC, user_token, id=''):
        self.id = self.set_id()
        self.name = name
        self.level = level
        self.race = race
        self.gender = gender
        self._class = _class
        self.hp = hp
        self.ac = ac
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intellegence = intellegence
        self.wisdom= wisdom
        self.charisma = charisma
        self.spellDC = spellDC
        self.user_token = user_token 

    def __repr__(self):
        return f'{self.name} level {self.level} {self._class} {self.race}'

    def set_id(self):
        return (secrets.token_urlsafe())

 # Creation of API Schema via the Marshmallow Object
class UserSchema(ma.Schema):
    class Meta:
        fields = ['id','first_name', 'last_name','username', 'email','password','token']

user_schema = UserSchema()

class CharacterSchema(ma.Schema):
    class Meta:
        fields = ['id','name', 'level', 'race','gender','_class','hp', 'ac', 'strength','dexterity','constitution','intellegence','wisdom', 'charsima', 'spellDC','user_token']

character_schema = CharacterSchema()

characters_schema = CharacterSchema(many = True)
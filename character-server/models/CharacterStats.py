from app import db

class CharacterStats(db.Model):

    __tablename__  = 'characters_stats'

    id = db.Column(db.Integer, primary_key= True)

    hp = db.Column(db.Numeric(precision = 2), nullable=False)
    ac = db.Column(db.Numeric(precision = 2))
    strength = db.Column(db.Numeric(precision = 2), nullable=False)
    dexterity = db.Column(db.Numeric(precision = 2), nullable=False)
    constitution = db.Column(db.Numeric(precision = 2), nullable=False)
    intelligence = db.Column(db.Numeric(precision = 2), nullable=False)
    wisdom = db.Column(db.Numeric(precision = 2), nullable=False)
    charisma = db.Column(db.Numeric(precision = 2), nullable=False)
    spellDC = db.Column(db.Numeric(precision = 2))

    character_id = db.Column(db.String, db.ForeignKey('character.id'), nullable = False)
    character = db.relationship('CharacterModel', back_populates='stats')

    def __repr__(self):
      return f'{self.name} level {self.level} {self._class} {self.race}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

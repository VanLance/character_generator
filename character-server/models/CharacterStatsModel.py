from app import db

class CharacterStatsModel(db.Model):

    __tablename__  = 'character_stats'

    id = db.Column(db.Integer, primary_key= True)

    hp = db.Column(db.Integer, nullable=False)
    ac = db.Column(db.Integer)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    spellDC = db.Column(db.Integer)

    # character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable = False)
    # character = db.relationship('CharacterModel', back_populates='stats')

    def __repr__(self):
      return f'<{self.character.name} stats: {self.__dict__()}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, dict):
      for att, v in dict.items():
          setattr(self, att, v)

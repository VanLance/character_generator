from app import db

from character_creation.index import createCharacter, runCreate

class CharacterModel(db.Model):

    __tablename__  = 'character'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    level = db.Column(db.Numeric(precision = 2))
    race = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    _class = db.Column(db.String(150))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    user = db.relationship('UserModel', back_populates='characters') 

    stats_id = db.Column(db.Integer, db.ForeignKey('character_stats.id'), nullable = False)
    stats = db.relationship('CharacterStatsModel', backref='character')

    def __repr__(self):
        return f'{self.name} level {self.level} {self._class} {self.race}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, dict):
        for att, v in dict.items():
            setattr(self, att, v)

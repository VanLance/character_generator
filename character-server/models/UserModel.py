from app import db

from werkzeug.security import generate_password_hash, check_password_hash

followers = db.Table('followers',
  db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
  db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))           
)

class UserModel(db.Model):

  __tablename__  = 'user'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String, unique = True, nullable = False)
  email = db.Column(db.String, unique = True, nullable = False)
  password_hash = db.Column(db.String, nullable = False)
  first_name = db.Column(db.String)
  last_name = db.Column(db.String)
  followed = db.relationship('UserModel', 
    secondary=followers, 
    primaryjoin = followers.c.follower_id == id,
    secondaryjoin = followers.c.followed_id == id,
    backref = db.backref('followers', lazy='dynamic'),
    lazy='dynamic' 
  )

  characters = db.relationship('CharacterModel', back_populates='user', lazy='dynamic', cascade='all, delete')
  def __repr__(self):
    return f'<User: {self.username}>'
  
  def hash_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  
  def from_dict(self, dict):
    password = dict.pop('password')
    self.hash_password(password)
    for k,v in dict.items():
      setattr(self, k, v)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def is_following(self, user):
    return self.followed.filter(user.id == followers.c.followed_id).count() > 0
  
  def follow_user(self, user):
    if not self.is_following(user):
      self.followed.append(user)
      self.save()

  def unfollow_user(self, user):
    if self.is_following(user):
      self.followed.remove(user)
      self.save()
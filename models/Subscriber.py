import sys
sys.path.append('..')

from datetime import datetime

from app import db

class Subscriber(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __init__(self, name, email):
    self.name = name
    self.email = email

  def to_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'created_at': self.created_at,
    }
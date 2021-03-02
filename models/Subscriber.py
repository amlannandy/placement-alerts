from datetime import datetime

from .. import db

class Subscriber(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __init__(self, name, email):
    self.name = name
    self.email = email
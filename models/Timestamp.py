import sys
sys.path.append('..')

from datetime import datetime

from app import db

class Timestamp(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  count = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __init__(self, count):
    self.count = count

  def to_json(self):
    return {
      'id': self.id,
      'count': self.count,
      'created_at': self.created_at,
    }
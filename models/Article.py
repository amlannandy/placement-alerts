import sys
sys.path.append('..')

from datetime import datetime

from app import db

class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False, unique=True)
  content = db.Column(db.String(2000), nullable=False)
  url = db.Column(db.String(300), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __init__(self, title, content, url):
    self.title = title
    self.content = content
    self.url = url

  def to_json(self):
    return {
      'id': self.id,
      'title': self.title,
      'content': self.content,
      'url': self.url,
      'created_at': self.created_at,
    }
from app import app, db

from models.Article import Article
from models.Timestamp import Timestamp
from models.Subscriber import Subscriber

with app.app_context():
  db.create_all()
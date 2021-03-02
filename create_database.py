from app import app, db
from models.Subscriber import Subscriber

with app.app_context():
  db.create_all()
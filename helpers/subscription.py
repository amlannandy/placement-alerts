import sys
sys.path.append('..')

from app import db
from models.Subscriber import Subscriber

def find_by_email(email):
  return Subscriber.query.filter_by(email=email).first()

def save(subscriber):
  db.session.add(subscriber)
  db.session.commit()
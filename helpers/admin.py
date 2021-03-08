import sys
sys.path.append('..')

import os
from functools import wraps
from flask import request, jsonify

from app import db
from models.Article import Article
from models.Timestamp import Timestamp
from models.Subscriber import Subscriber

# Use this decorator on routes which only admins should be able to access
def admin_only(fun):
  @wraps(fun)
  def wrap(*args, **kwargs):

    # if request does not have a password at all
    try:
      password = request.headers['Admin-Password']
    except:
      response = {
        'success': False,
        'msg': 'Please add an admin password to access this route',
      }
      return jsonify(response), 401

    # If password is an empty string
    if not password:
      response = {
        'success': False,
        'msg': 'Please add an admin password to access this route',
      }
      return jsonify(response), 401

    # If request has a wrong password
    if password != os.getenv('ADMIN_PASSWORD'):
      response = {
        'success': False,
        'msg': 'Unauthorized. Wrong admin password',
      }
      return jsonify(response), 401

    # Else continue
    return fun(*args, **kwargs)
  return wrap

def fetch_all_users():
  return Subscriber.query.order_by(Subscriber.created_at).all()

def fetch_all_user_emails():
  subs = Subscriber.query.order_by(Subscriber.created_at).all()
  return list(map(lambda sub: sub.email, subs))

def fetch_all_articles():
  return Article.query.all()

def find_by_title(title):
  return Article.query.filter_by(title=title).first()

def save_article_from_json(json_article):
  article = Article(title=json_article['title'][:99], content='', url='')
  db.session.add(article)
  db.session.commit()

def fetch_all_timestamps():
  return Timestamp.query.order_by(Timestamp.created_at).all()

# For maintaining records of when the scheduler ran
def add_timestamp(count):
  timestamp = Timestamp(count=count)
  db.session.add(timestamp)
  db.session.commit()
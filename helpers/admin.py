import sys
sys.path.append('..')

from app import db
from models.Article import Article
from models.Subscriber import Subscriber

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
  article = Article(title=json_article['title'], content=json_article['content'], url=json_article['url'])
  db.session.add(article)
  db.session.commit()
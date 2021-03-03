import sys
sys.path.append('..')

from flask import Blueprint, jsonify

from scripts.scrapper import extract_articles
from helpers.send_email import send_article_email
from helpers.admin import admin_only, fetch_all_articles, save_article_from_json, find_by_title, fetch_all_user_emails, fetch_all_users

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/subscribers-list', methods=['GET'])
@admin_only
def view_all_subscribers():
  subscribers = fetch_all_users()
  response = {
    'success': True,
    'data': list(map(lambda s: s.to_json(), subscribers)),
  }
  return jsonify(response), 200

@admin.route('/articles-list', methods=['GET'])
@admin_only
def view_all_articles():
  articles = fetch_all_articles()
  response = {
    'success': True,
    'data': list(map(lambda a: a.to_json(), articles)),
  }
  return jsonify(response), 200

@admin.route('/extract-data', methods=['GET'])
@admin_only
def extract_data():
  articles = extract_articles()
  user_emails = fetch_all_user_emails()
  count = 0
  for article in articles:
    in_db = find_by_title(article['title'])
    if not in_db:
      count += 1
      save_article_from_json(article)
      send_article_email(user_emails, article)

  response = {
    'success': True,
    'msg': f'{count} new articles sent',
  }
  return jsonify(response), 200
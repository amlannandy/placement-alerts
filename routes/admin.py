import sys
sys.path.append('..')

from flask import Blueprint, jsonify

from models.Subscriber import Subscriber
from scripts.scrapper import extract_articles

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/subscribers-list', methods=['GET'])
def view_all_subscribers():
  subscribers = Subscriber.query.order_by(Subscriber.created_at).all()
  response = {
    'success': True,
    'data': list(map(lambda s: s.to_json(), subscribers)),
  }
  return jsonify(response), 200

@admin.route('/extract-data', methods=['GET'])
def extract_data():
  articles = extract_articles()
  response = {
    'success': True,
    'data': articles,
  }
  return jsonify(response), 200
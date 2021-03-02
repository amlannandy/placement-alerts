import sys
sys.path.append('..')

from flask import Blueprint, jsonify, request

from models.Subscriber import Subscriber
from helpers.subscription import find_by_email, save

subscription = Blueprint('subscription', __name__, url_prefix='/subscription')

@subscription.route('/', methods=['POST'])
def subscribe_new_user():
  '''
  Add a new user to the subscription list
  '''
  data = request.get_json()

  # Check if no data is sent at all
  if not data:
    response = {
      'success': False,
      'msg': 'Please provide name and email',
    }
    return jsonify(response), 400

  # Check if a key is missing
  try:
    name = data['name']
    email = data['email']
  except KeyError as err:
    response = {
      'success': False,
      'msg': f'Please provide {str(err)}'
    }
    return jsonify(response), 400

  # Check if this email has already subscribed
  subscriber = find_by_email(email)
  if subscriber:
    response = {
      'success': False,
      'msg': 'Already subscribed to mailing list'
    }
    return jsonify(response), 409

  subscriber = Subscriber(name=name, email=email)
  save(subscriber)

  response = {
    'success': True,
    'msg': 'Successfully subscribed to mailing list'
  }
  return jsonify(response), 200
  
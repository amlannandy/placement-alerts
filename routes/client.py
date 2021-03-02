import sys
sys.path.append('..')

from flask import Blueprint, render_template

client = Blueprint('client', __name__)

@client.route('/', methods=['GET'])
def view_all_subscribers():
  return render_template('subscribe.html')
import sys

from flask.helpers import flash
sys.path.append('..')

from flask import Blueprint, request, render_template
from wtforms import Form, TextField, validators

from models.Subscriber import Subscriber
from helpers.subscription import find_by_email, save, delete_by_email

subscription = Blueprint('subscription', __name__)

class SubscriptionForm(Form):
  name = TextField('Name', validators=[validators.required()])
  email = TextField('Email', validators=[validators.required(), validators.Length(min=6, max=35)])

  # Open index page of website
  @subscription.route('/', methods=['GET', 'POST'])
  def open_subscribe_page():
    form = SubscriptionForm(request.form)

    if request.method == 'POST':

      name=request.form['name']
      email=request.form['email']

      subscriber = find_by_email(email)

      if subscriber:
        flash('Oops! Looks like you have already subscribed to mailing list', 'warning')
      else:
        subscriber = Subscriber(name=name, email=email)
        save(subscriber)
        flash('Success! You have now subscribed to the mailing list', 'success')
    
    return render_template('subscribe.html', form=form)

@subscription.route('/unsubscribe/<email>', methods=['GET', 'POST'])
def open_unsubscribe_page(email):

  if request.method == 'POST':

    # Check if a subsriber with that email exists
    subscriber = find_by_email(email)
    if not subscriber:
      flash('Oops! Looks like you have already unsubscribed', 'warning')
    else:
      delete_by_email(email)
      flash('Success! You will no longer get these emails', 'success')
  
  return render_template('unsubscribe.html')  
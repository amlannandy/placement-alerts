import sys
sys.path.append('..')

from flask import render_template
from flask_mail import Message

from app import mail

def send_welcome_email(user):
  msg = Message('Welcome to Placement Alerts', sender='alerts@placement.in', recipients=[user['email']])
  msg.html = render_template('welcome_email.html', name=user['name'], email=user['email'])
  try:
    mail.send(msg)
  except ConnectionRefusedError as err:
    print(err)
    raise ConnectionRefusedError 

# def send_article_email(recipient, article, user):
#   msg = Message(title, sender='alerts@placement.com', recipients=[recipient])
#   msg.html = render_template(template, name='Amlan Singh', email='test@gmail.com')
#   try:
#     mail.send(msg)
#   except ConnectionRefusedError as err:
#     print(err)
#     raise ConnectionRefusedError
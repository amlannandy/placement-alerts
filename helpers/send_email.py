import sys
sys.path.append('..')

import os
from flask import render_template
from flask_mail import Message

from app import mail

def send_welcome_email(user):
  msg = Message('Welcome to Placement Alerts', sender=os.environ.get('MAIL_DEFAULT_SENDER'), recipients=[user['email']])
  msg.html = render_template('welcome_email.html', name=user['name'], email=user['email'])
  try:
    mail.send(msg)
  except ConnectionRefusedError as err:
    print(err)
    raise ConnectionRefusedError 

def send_article_email(recipients, article):
  msg = Message(article['title'], sender=os.environ.get('MAIL_DEFAULT_SENDER'), bcc=recipients)
  msg.html = render_template('article_email.html', 
    title=article['title'],
    content=article['content'],
    url=article['url'],
  )
  try:
    mail.send(msg)
  except ConnectionRefusedError as err:
    print(err)
    raise ConnectionRefusedError
import os
from flask import Flask
from dotenv import load_dotenv
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

# Init db
db = SQLAlchemy()

# Init Flask app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config["JWT_SECRET_KEY"] = "super-secret"

# Load environment variables
load_dotenv()

# Set up email service
app.config.update(dict(
  DEBUG = True,
  MAIL_SERVER = os.getenv('MAIL_SERVER'),
  MAIL_PORT = os.getenv('MAIL_PORT'),
  MAIL_USE_TLS = True,
  MAIL_USE_SSL = False,
  MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
  MAIL_PASSWORD = os.getenv('SENDGRID_API_KEY'),
  MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER'),
))
mail = Mail(app)

# Scheduler to scrape data every 24 hours
from scripts.data_extraction import extract_data_from_source

sched = BackgroundScheduler(daemon=True)
sched.add_job(extract_data_from_source, 'interval', hours=24)
sched.start()

# Import blueprints
from routes.admin import admin as AdminBlueprint
from routes.subscription import subscription as SubscriptionBlueprint

app.register_blueprint(AdminBlueprint)
app.register_blueprint(SubscriptionBlueprint)

# Setup and init db
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Init db
db = SQLAlchemy()

# Init app
app = Flask(__name__)

# Setup and init db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
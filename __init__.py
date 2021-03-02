from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Init db
db = SQLAlchemy()

# Init app
app = Flask(__name__)
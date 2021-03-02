from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Init db
db = SQLAlchemy()

# Init Flask app
app = Flask(__name__)

# Import blueprints
from routes.admin import admin as AdminBlueprint
from routes.subscription import subscription as SubscriptionBlueprint

app.register_blueprint(AdminBlueprint)
app.register_blueprint(SubscriptionBlueprint)

# Setup and init db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
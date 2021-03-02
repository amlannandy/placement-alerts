from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Init db
db = SQLAlchemy()

# Init Flask app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# Import blueprints
from routes.admin import admin as AdminBlueprint
from routes.subscription import subscription as SubscriptionBlueprint

app.register_blueprint(AdminBlueprint)
app.register_blueprint(SubscriptionBlueprint)

# Setup and init db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

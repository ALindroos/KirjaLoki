from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# tulostaa SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

#Sovelluksen toiminallisuus
from application import views

from application.books import models
from application.books import views

from application.auth import models
from application.auth import views

#Kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Create database
db.create_all()
from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# tulostaa SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.books import models
from application.books import views

from application.auth import models
from application.auth import views


db.create_all()
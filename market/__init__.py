#This file is used to make from directory package where other modules can import data

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #File that will be recognized as database
app.config['SECRET_KEY'] = 'e20d78b21c8345a7be45d8c8'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
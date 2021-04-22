from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'c2944b205b9d8af28c5bf297'
# DATABASE INITIALISATION
db=SQLAlchemy(app)

from market import route
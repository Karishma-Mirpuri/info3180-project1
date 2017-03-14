from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] = "53cr3tk3y"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views

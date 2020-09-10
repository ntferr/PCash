from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

CORS(app)

app.secret_key = ""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymsql://root:root@localhost/db_icash'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
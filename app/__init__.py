import os
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import app_config


app = Flask(__name__)
CORS(app)
app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
db = SQLAlchemy(app)


from app import routes, models

with app.app_context():
    db.create_all()
    
# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app


app = create_app(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)

from app import routes, models

with app.app_context():
    # create all tables
    db.create_all()

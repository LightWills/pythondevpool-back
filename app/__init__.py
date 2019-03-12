from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from config import app_config


db = SQLAlchemy()
def create_app(config_name):
    from app.models import User

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    ### ROUTES ###
    @app.route("/users", methods=['GET', 'POST'])
    def users():
        if request.method == 'GET':
            users = [user.to_dict() for user in db.session.query(User)]
            return jsonify(users), 200

        if request.method == 'POST':
            user = User(
                name=request.json['name'],
                lastname=request.json['lastname'],
                login=request.json['login'],
                desc=request.json['desc']
            )
            db.session.add(user)
            db.session.commit()
            return jsonify(request.json), 201

    @app.route("/users/<int:id>", methods=['GET'])
    def user(id):
        user = db.session.query(User).get(id)
        if user:
            return jsonify(user.to_dict()), 200

        return abort(404)

    return app

from app import app, db
from app.models import User
from flask import request, jsonify, abort


@app.route("/users", methods=['GET', 'POST'])
def add_user():
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
def show_user(id):
    user = db.session.query(User).get(id)
    if user:
        return jsonify(user.to_dict()), 200

    return abort(404)
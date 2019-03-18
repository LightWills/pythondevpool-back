from app import app, db
from app.models import User
from flask import request, jsonify, abort


@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = [user.to_dict() for user in db.session.query(User)]
        return jsonify(users), 200

    if request.method == 'POST':
        try:
            user = User.from_json(request.json)
        except:
            return abort(400)          
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201

@app.route("/users/<int:id>", methods=['GET', 'DELETE'])
def user(id):
    user = db.session.query(User).get(id)
    if not user:
        return abort(404)
    
    if request.method == 'GET':
        return jsonify(user.to_dict()), 200

    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return "OK", 200

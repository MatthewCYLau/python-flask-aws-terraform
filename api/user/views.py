from api import app
from api.user.models import User
from flask import jsonify, request
from api import db


@app.route("/users", methods=["GET"])
def list_users():

    try:
        users = User.query.all()
        return jsonify(users), 200
    except:
        return "Error fetching data", 500


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):

    try:
        user = User.query.get_or_404(id)
        return jsonify(user), 200
    except:
        return "Not found", 404


@app.route("/users", methods=["POST"])
def add_user():

    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]

    new_user = User(name=name, email=email, password=password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user), 201
    except:
        return "Error creating user", 500


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):

    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return "OK", 200
    except:
        return "Error deleting user", 500


@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):

    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]

    try:
        user = User.query.get_or_404(id)
        user.name = name
        user.email = email
        user.password = password

        db.session.commit()
        return "OK", 200
    except:
        return "Error updating user", 500

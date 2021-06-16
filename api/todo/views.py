import requests
import random
from api import app
from api.todo.models import Todo
from flask import jsonify, request
from api import db


@app.route("/todos", methods=["GET"])
def list_todos():

    try:
        todos = Todo.query.all()
        return jsonify(todos), 200
    except:
        return "Error fetching data", 500


@app.route("/todos/<int:id>", methods=["GET"])
def get_todo(id):

    try:
        todo = Todo.query.get_or_404(id)
        return jsonify(todo), 200
    except:
        return "Not found", 404


@app.route("/todos", methods=["POST"])
def add_todo():

    id = random.randint(1, 1000)
    name = request.json["name"]
    description = request.json["description"]
    completed = False

    new_todo = Todo(id=id, name=name, description=description, completed=completed)

    try:
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(new_todo), 201
    except:
        return "Error creating todo", 500


@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):

    try:
        todo = Todo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()
        return "OK", 200
    except:
        return "Error deleting todo", 500


@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):

    name = request.json["name"]
    description = request.json["description"]
    completed = request.json["completed"]

    try:
        todo = Todo.query.get_or_404(id)
        todo.name = name
        todo.description = description
        todo.completed = completed

        db.session.commit()
        return "OK", 200
    except:
        return "Error updating todo", 500

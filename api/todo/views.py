import requests
import random
from api import app
from api.todo.models import Todo
from flask import jsonify, request
from api import db


@app.route("/ping")
def ping():

    return "pong!"


@app.route("/todos", methods=["GET"])
def list_todos():

    try:
        todos = Todo.query.all()
        return jsonify(todos), 200
    except:
        return "Error fetching data", 500


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

from api import app
from api.todo.models import Todo
import requests
from flask import jsonify
from api import db


todos = [
    {"id": 1, "name": "foo", "description": "bar"},
    {"id": 2, "name": "fooo", "description": "baar"},
]


@app.route("/ping")
def ping():

    return "pong!"


@app.route("/todos", methods=["GET"])
def list_todos():

    # todos = Todo.query.all()
    res = requests.get("https://jsonplaceholder.typicode.com/posts")

    if res.status_code == 200:
        return jsonify(res.json()), 200
    else:
        return "Error fetching data", 500


@app.route("/todos", methods=["POST"])
def add_todo():
    # todo = Todo(id=1, name="foo", description="bar", completed=False)
    # db.session.add(todo)
    # db.session.commit()

    data = todos[0]
    return jsonify(data), 201

from api import app
from api.models import Todo
from api import db


@app.route("/ping")
def ping():

    return "pong!"


@app.route("/todos", methods=["GET"])
def list_todos():

    todos = Todo.query.all()

    for todo in todos:
        print(todo)

    return "List todos"


@app.route("/todos", methods=["POST"])
def add_todo():
    todo = Todo(name="foo", description="bar", completed=False)
    db.session.add(todo)
    db.session.commit()

    return "Added todo"

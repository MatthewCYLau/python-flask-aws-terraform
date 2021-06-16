import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# when running app inside docker compose, connect to @db:5432
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:password@localhost:5432/flaskdb"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


from api.todo.models import Todo

db.create_all()
db.session.commit()


@app.route("/ping")
def ping():

    return "pong!"


from api.todo import views

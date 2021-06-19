import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv(".env")

app = Flask(__name__)


db_address = os.environ.get("DB_ADDRESS")
db_name = os.environ.get("DB_NAME")
postgres_username = os.environ.get("POSTGRES_USERNAME")
postgres_password = os.environ.get("POSTGRES_PASSWORD")


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{postgres_username}:{postgres_password}@{db_address}:5432/{db_name}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


from api.todo.models import Todo

db.create_all()
db.session.commit()


@app.route("/ping")
def ping():

    return "pong!"


from api.todo import views

import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv(".env")

app = Flask(__name__)


db_address = os.environ.get("DB_ADDRESS")
db_name = os.environ.get("DB_NAME")
db_port = "5432"
postgres_username = os.environ.get("POSTGRES_USERNAME")
postgres_password = os.environ.get("POSTGRES_PASSWORD")


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{postgres_username}:{postgres_password}@{db_address}:{db_port}/{db_name}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


from api.todo.models import Todo
from api.user.models import User


# no need to set-up database during image build process
if os.environ.get("ENV") != "CI":
    db.create_all()
    db.session.commit()


@app.route("/ping")
def ping():

    return "pong!"


from api.todo import views
from api.user import views

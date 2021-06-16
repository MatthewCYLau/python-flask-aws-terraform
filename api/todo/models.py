from dataclasses import dataclass
from api import db
import json


@dataclass
class Todo(db.Model):

    id: int
    name: str
    description: str
    completed: bool

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean)

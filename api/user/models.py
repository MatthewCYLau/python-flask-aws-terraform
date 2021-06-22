from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import ARRAY
from dataclasses import dataclass
from api import db
from sqlalchemy.orm import relationship
from api.todo.models import Todo
import uuid


@dataclass
class User(db.Model):

    __tablename__ = "user"

    id: UUID
    name: str
    email: str
    password: bool
    todos: ARRAY(Todo)

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    todos = relationship("Todo")

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, ForeignKey
from dataclasses import dataclass
from api import db
import uuid


@dataclass
class Todo(db.Model):

    __tablename__ = "todo"

    id: UUID
    name: str
    description: str
    completed: bool
    user_id: str

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)
    user_id = Column(UUID, ForeignKey("user.id"))

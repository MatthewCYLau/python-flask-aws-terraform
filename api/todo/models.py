from api import db


class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean)

    def __repr__(self):
        return self.name

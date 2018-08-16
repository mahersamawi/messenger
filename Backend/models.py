from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TODO Design questions, DB Model and representation


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), unique=False, nullable=False)
    intended_room = db.Column(db.String(120), unique=False, nullable=False)
    message_text = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, sender, intended_room, message_text):
        self.sender = sender
        self.intended_room = intended_room
        self.message_text = message_text

    def __repr__(self):
        return '<Message %r>' % self.message_text

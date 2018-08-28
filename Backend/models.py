from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TODO Design questions, DB Model and representation


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), unique=False, nullable=False)
    intended_room = db.Column(db.String(120), unique=False, nullable=False)
    message_text = db.Column(db.String(120), unique=False, nullable=False)
    time_sent = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, sender, intended_room, message_text, time_sent):
        self.sender = sender
        self.intended_room = intended_room
        self.message_text = message_text
        self.time_sent = time_sent

    def __repr__(self):
        return '<Message %r>' % self.message_text


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    token = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id, date_joined, email, username):
        self.id = id
        self.date_joined = date_joined
        self.email = email
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    members = db.Column(db.String(80), unique=False, nullable=False)
    room_messages = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id, members, room_messages, name):
        self.id = id
        self.members = members
        self.room_messages = room_messages
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name

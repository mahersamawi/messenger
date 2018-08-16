import logging
from flask_socketio import SocketIO, send, join_room, leave_room
from flask import Flask, request, jsonify, make_response
from routes import message_bp
from models import db

LOG_TO_FILE = False
LEVEL = logging.INFO
if LOG_TO_FILE:
    logging.basicConfig(filename='logger.log', filemode='w',
                        format='%(levelname)s:%(message)s', level=LEVEL)
else:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=LEVEL)

app = Flask(__name__)
socketio = SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
with app.app_context():
    db.init_app(app)
    db.create_all()
app.register_blueprint(message_bp)

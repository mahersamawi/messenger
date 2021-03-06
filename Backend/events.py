import logging
from flask_socketio import SocketIO, send, join_room, leave_room
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from app import socketio
from models import Message, db


@socketio.on("message")
def message_handler(msg):
    """
    Message hangler that whenever a message is received it is sent to the proper room. 
    :param msg: Dictonary containing the message contebts and intended roon
    """
    logging.info("Message Text: %s" % msg['msg'])

    message_entry = Message(request.sid, msg['room'], msg['msg'], msg['time'])
    if msg['msg'] != "User has connected!":
        logging.info("About to add to DB")
        db.session.add(message_entry)
        db.session.commit()
        logging.info("Added to DB")
    send(msg['msg'], room=msg['room'])


@socketio.on('join')
def on_join(data):
    """
    Join handler, when a user wants to join a specific room
    """
    username = request.sid
    room = data
    join_room(room)
    logging.info(username + ' has entered the room.')
    send(username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    """
    Leave handler, when a user wants to leave a specific room
    """
    username = request.sid
    room = data
    leave_room(room)
    logging.info(username + ' has left the room.')
    send(username + ' has left the room.', room=room)

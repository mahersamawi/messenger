import json
import socket
import datetime
import urllib.request
import logging
import time
from flask_socketio import SocketIO, send, join_room, leave_room
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
socketio = SocketIO(app)
LOG_TO_FILE = False
LEVEL = logging.INFO


if LOG_TO_FILE:
    logging.basicConfig(filename='logger.log', filemode='w',
                        format='%(levelname)s:%(message)s', level=LEVEL)
else:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=LEVEL)


@app.route("/conversations", methods=["GET"])
def get_conversations():
    """
    Return a users associated conversations 
    Should be continuously be polled to get the the most recent messages
    """
    user_token = get_parameter(request, "access_token")
    if user_token is None:
        return make_response(jsonify("Access Token Needed"), 404)

    # Get the user conversations from the database


@app.route("/profile", methods=["GET"])
def get_profile():
    """
    Get a user's profile
    """
    user_token = get_parameter(request, "access_token")
    if user_token is None:
        return make_response(jsonify("Access Token Needed"), 404)


@app.route("/create_user", methods=["POST"])
def create_user():
    """
    Create a user 
    Information should be encrypted in the URL added to db
    Encrypt the information 
    """
    return make_response((jsonify("User Created!")))
    pass


@app.route("/send_message", methods=["POST"])
def send_message():
    """
    Send a messsage to a user 
    @receiver id or convo ID
    @message text
    What this should is get the message
        update datatbase
        maybe ack?
        convos endpoint will be polled and that reads from the db to update the convo
    """
    # user_token = get_parameter(request, "access_token")
    # if user_token is None:
    #     return make_response(jsonify("Access Token Needed"), 404)
    convo_id = get_parameter(request, 'convo_id')
    message_text = get_parameter(request, 'message_text')
    if convo_id is None or message_text is None:
        logging.debug("Convo id or message text missing")
        return make_response((jsonify("Need convo_id and message_text")))

    logging.info("Conversation ID is: %s" % str(convo_id))
    logging.info("Message Text: %s" % str(message_text))

    # Update database with the information

    return make_response((jsonify("Message sent!")))


def get_parameter(url_to_parse, parameter_to_get):
    """
    Function to get paramter from URL
    :param url_to_parse: The request that contains the parameter
    :return: The value of the parameter. Otherwise None
    """
    return url_to_parse.values.get(parameter_to_get, None)


@socketio.on("message")
def message_handler(msg):
    print("Message is: " + msg)
    send(msg, broadcast=False)

@socketio.on('join')
def on_join(data):
    print("In join")
    username = request.sid
    room = data
    print(request.sid)
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = request.sid
    room = data
    leave_room(room)
    send(username + ' has left the room.', room=room)



def get_ip():
    """
    Function that gets IP of local machine so server can be used on that IP instead of localhost
    :return: The IP of the machine
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    # Returns tuple of ip and port
    return s.getsockname()[0]

if __name__ == "__main__":
    #host_ip = str(get_ip())
    # Uses HTTP on ip
    host_ip = "127.0.0.1"
    #app.run(host=host_ip, threaded=True)
    socketio.run(app, host=host_ip)
    # Uses HTTPS
    # app.run(ssl_context='adhoc', host=host_ip)
    # Uses HTTP on localhost
    # app.run()

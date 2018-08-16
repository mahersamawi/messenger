import json
import socket
import datetime
import urllib.request
import logging
import time
from flask import Flask, request, jsonify, make_response, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models import *

message_bp = Blueprint('message', __name__)


@message_bp.route("/conversations", methods=["GET"])
def get_conversations():
    """
    Return a users associated conversations 
    Should be continuously be polled to get the the most recent messages
    """
    user_token = get_parameter(request, "access_token")
    if user_token is None:
        return make_response(jsonify("Access Token Needed"), 404)

    # Get the user conversations from the database


@message_bp.route("/profile", methods=["GET"])
def get_profile():
    """
    Get a user's profile
    """
    user_token = get_parameter(request, "access_token")
    if user_token is None:
        return make_response(jsonify("Access Token Needed"), 404)


@message_bp.route("/create_user", methods=["POST"])
def create_user():
    """
    Create a user 
    Information should be encrypted in the URL added to db
    Encrypt the information 
    """
    return make_response((jsonify("User Created!")))
    pass


@message_bp.route("/send_message", methods=["POST"])
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
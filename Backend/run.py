import socket
from app import app, socketio
from events import *


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
    host_ip = str(get_ip())
    # Uses HTTP on ip
    #host_ip = "127.0.0.1"
    #app.run(host=host_ip, threaded=True)
    socketio.run(app, host=host_ip)
    # Uses HTTPS
    # app.run(ssl_context='adhoc', host=host_ip)
    # Uses HTTP on localhost
    # app.run()

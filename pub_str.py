# pub.py
import zmq
import time
import random

host = "*"
port = "5001"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.PUB)

# Binds the socket to a predefined port on localhost
socket.bind("tcp://{}:{}".format(host, port))
topic = "bboxes"

while True:
    messagedata = str(random.randrange(1,215) - 80)
    socket.send_string(f"{topic} {messagedata}")
    print (f"{topic} {messagedata}")
    time.sleep(1)
# Sends a string message
socket.send_string("hello")
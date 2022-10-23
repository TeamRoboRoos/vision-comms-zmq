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
topic = "our-topic"

while True:
    messagedata = str(random.randrange(1,215) - 80)
    json_msg = {"message": messagedata}

    # First send the topic string with the flag to do send multpart.
    socket.send_string(topic, flags=zmq.SNDMORE)
    
    # Then send the data. As it doesnt have zmq.SNDMORE, this will terminate the recv.
    socket.send_json(json_msg) 
    
    print (f"{topic} {json_msg}")
    time.sleep(1)

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

img_width = 640
img_height = 640
num_object_categories = 12


def generate_bbox():
    '''Generates a single random bounding box'''
    x1 = random.randrange(0,img_width-1)
    y1 = random.randrange(0,img_height-1)
    
    x2 = random.randrange(x1,img_width)
    y2 = random.randrange(y1,img_height)
    
    prob = random.random()
    object_class = random.randrange(0,num_object_categories)

    return {
        'x1': x1,
        'y1': y1,
        'x2': x2,
        'y2': y2,
        'prob': prob,
        'object_class': object_class,
        'img_width': img_width,
        'img_height': img_height
    }
    
def generate_bboxes(max_bboxes=3):
    '''
    Randomly Generates a set of bboxes
    '''
    bboxes = []
    num_to_generate = random.randrange(0,max_bboxes)
    for _ in range(num_to_generate):
        bboxes.append(
            generate_bbox()
        )

    return {"bboxes": bboxes, 'num_bboxes': len(bboxes)}

while True:
    messagedata = str(random.randrange(1,215) - 80)
    
    json_msg = generate_bboxes()

    # First send the topic string with the flag to do send multpart.
    socket.send_string(topic, flags=zmq.SNDMORE)
    
    # Then send the data. As it doesnt have zmq.SNDMORE, this will terminate the recv.
    socket.send_json(json_msg) 
    
    print (f"{topic} {json_msg}")
    time.sleep(1)

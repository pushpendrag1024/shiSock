import socket
import base64
from random import sample,shuffle
import pickle
import time

def name_generator(_len_ = 16, onlyText = False):
    lower_case = list("abcdefghijklmnopqrstuvwxyz")
    upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special = list("!@#$%&*?")
    number = list("0123456789")

    if onlyText:
        _all_ = lower_case + upper_case
    else:
        _all_ = lower_case + upper_case + special + number
        
    shuffle(_all_)
    return "".join(sample(_all_,_len_))

count = 0
print("Test Started...")
while True:
    s = socket.socket()
    s.connect(("192.168.43.206",9600))

    name = name_generator(_len_ = 8, onlyText = True)

    ini = base64.b64encode(pickle.dumps(name))
    s.send(bytes(str(len(ini)).center(32,"-"),"utf-8"))
    s.send(ini)

    prepare_send_data = {
        "channel" : "test",
        "sender_name" : name,
        "target_name" : "SERVER",
        "data" : "Hello World"
    }

    prepare_for_send = base64.b64encode(pickle.dumps(prepare_send_data))
    s.send(bytes(str(len(prepare_for_send)).center(32,"-"),"utf-8"))
    s.send(prepare_for_send)

    count += 1
    print(count)

    # time.sleep(1)


# C@C/piBsKTAP9?C
    


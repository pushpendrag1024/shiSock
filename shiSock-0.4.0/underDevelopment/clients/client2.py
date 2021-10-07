import socket
import json
import base64
from rich import print as rprint

# @Cname
name = "swat"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",1234))

OBJECT = {
    "type" : "code-0.0.1-new",
    "sender_name" : name,
}

json_data = json.dumps(OBJECT)
# b_data = base64.b64encode(bytes(json_data,"utf-8"))

b_data = bytes(json_data, "utf-8")

s.send( bytes( f"{len(b_data)}".center(32,"`") , "utf-8" ) )
s.send(b_data)

data_len = int(s.recv(32).decode().strip("`"))
data = s.recv(data_len)

print(f"data : {data}")

q = base64.b64decode(data).decode()
jd = json.loads(q)
print(jd)
name = jd["data"]

print(f"name = {name}")

prepare_send = {
    "type" : "test",
    "sender_name" : name,
    "target_name" : "SERVER",
    "data" : "Hello From Client, Hurrah! It's Working"
}
b_data = json.dumps(prepare_send)
s.send( bytes( f"{len(b_data)}".center(32,"`") , "utf-8" ) )
s.send(bytes(b_data, "utf-8"))

data_len = int(s.recv(32).decode().strip("`"))
data = s.recv(data_len)
print(data)
data = base64.b64decode(data)
data = json.loads(data)
rprint("[green]Data From Server : ",end = "")
rprint(f"[purple]{data}")

data_len = int(s.recv(32).decode().strip("`"))
data = s.recv(data_len)
data = base64.b64decode(data)
data = json.loads(data)
rprint("[green]Data From Client : ",end = "")
rprint(f"[yellow]{data}")

prepare_send = {
    "type" : "DSP_MSG",
    "sender_name" : name,
    "target_name" : "shikhar",
    "data" : f"Hello From {name}, DSP_MSG functionality is Working Properly"
}
b_data = json.dumps(prepare_send)
s.send( bytes( f"{len(b_data)}".center(32,"`") , "utf-8" ) )
s.send(bytes(b_data, "utf-8"))


while True:
    None

from PySock import server

def client_msg(data):
    print(f"Message From : {data['sender_name']} => {data['data']}")

s = server(secure = False,debug = True)
s.SERVER("localhost",8888,10)
s.CREATE_CHANNEL("test")

new_client = []

while True:
    for d in s.conClients:
        if d not in new_client:
            s.SEND(d,"test","Hello From Server")
            new_client.append(d)

    s.LISTEN("test",client_msg)

    
from PySock import Sserver

def client_msg(data):
    print(f"Message From : {data['sender_name']} => {data['data']}")

s = Sserver(
    file = r's_yml.yaml',
    debug = False
    )
s.SERVER("localhost",1234,10)
s.CREATE_CHANNEL("test")

new_client = []

while True:
    for d in s.varifiedDevices:
        if d in s.conClients:       
            if d not in new_client:
                s.SEND(d,"test","Hello From Server")
                new_client.append(d)
        else:
            if d in new_client:
                new_client.remove(d)

    s.LISTEN("test",client_msg)

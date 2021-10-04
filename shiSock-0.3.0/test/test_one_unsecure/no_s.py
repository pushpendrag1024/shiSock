from PySock import server

def client_msg(data):
    print(f"Message From : {data['sender_name']} => {data['data']}")

s = server(debug = True)
s.SERVER("localhost",9999,9999)
s.CREATE_CHANNEL("test")

new_client = []

while True:
    s.LISTEN("test",client_msg)

    
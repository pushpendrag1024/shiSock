from PySock import Sclient

name = "swat"

def abc(data,con):
    print(f"Message from : {data['sender_name']} => {data['data']}")
    con.SEND("test","What are you doing!")

def client_msg(data,con):
    print(f"Message From : {data['sender_name']} => {data['data']}")
    con.SEND_TO_CLIENT(target_name = data["sender_name"], data = f"Hello From {name}")

c = Sclient(client_name = name, file = r'c2_yml.yaml', debug = False)
c.CLIENT("localhost",1234)
c.CREATE_CHANNEL("test")

count = 0
while True:
    c.LISTEN( channel = "test", function = abc, args = (c,) )
    c.LISTEN( channel = "DSP_MSG", function = client_msg, args = (c,))

    if count == 0:
        if "swat" in c.HS_Devices:
            c.SEND_TO_CLIENT(target_name = "swat", data = "Hello, what are you doing.")
            count += 1

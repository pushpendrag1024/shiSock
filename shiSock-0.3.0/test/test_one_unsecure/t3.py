from PySock import client

def abc(data,con):
    print(f"Message from {data['sender_name']} : {data['data']}")
    con.SEND("test","Very Happy")

c = client(client_name = "varsha", debug = True)
c.CLIENT("localhost",1234)
c.CREATE_CHANNEL("test")
while True:
    c.LISTEN( channel = "test", function = abc, args = (c,) )
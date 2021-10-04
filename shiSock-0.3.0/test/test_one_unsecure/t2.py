from PySock import client

def abc(data,con):
    print(f"Message from {data['sender_name']} : {data['data']}")
    con.SEND("test","Hurrah! it's working.")

def client_msg(data):
    print(f"Message from : {data['sender_name']} => {data['data']}")

c = client(client_name = "swat", debug = True)
c.CLIENT("localhost",8888)
c.CREATE_CHANNEL("test")
while True:
    c.LISTEN( channel = "test", function = abc, args = (c,) )

    c.LISTEN( channel = "DSP_MSG", function = client_msg)
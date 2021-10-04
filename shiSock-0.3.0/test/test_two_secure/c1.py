from PySock import Sclient

name = "shikhar"

def abc(data,con):
    print(f"Message from : {data['sender_name']} => {data['data']}")
    con.SEND("test","Hello!")

def client_msg(data):
    print(f"Message from : {data['sender_name']} => {data['data']}")

c = Sclient(client_name = name, file = r'c1_yml.yaml', debug = False)
c.CLIENT("localhost",1234)
c.CREATE_CHANNEL("test")

c.HANDSHAKE(target_name = "swat")
count = 0
while True:
    c.LISTEN( channel = "test", function = abc, args = (c,) )
    c.LISTEN( channel = "DSP_MSG", function = client_msg)

    if count == 0:
        if c.check("swat") in c.HS_Devices:
            c.SEND_TO_CLIENT(target_name = "swat", data = "Hello, what are you doing.")
            count += 1

        


    

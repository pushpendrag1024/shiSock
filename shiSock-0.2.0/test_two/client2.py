import PySock

run = True

def sample_func(data):
    print(data)

def client_func(data,con):
    print(f"Message From Client : {data}")
    con.SEND_TO_CLIENT(data["sender_name"],"Hello From Swat")

c = PySock.client(
   client_name=  "swat",
   DSP_enable= True,
   file = r'client1y.yaml',
   debug = True,
   rememberServer = True
   )
c.CLIENT("localhost",1234)
c.CREATE_CHANNEL("test")
c.SEND(channel = "test", data = "Hello, World!")
print("LISTENING...")
while run:
    c.LISTEN("test",sample_func)

    c.LISTEN("DSP_MSG", client_func, (c,))

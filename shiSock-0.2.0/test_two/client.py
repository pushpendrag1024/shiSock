import PySock

run = True

def sample_func(data):
    print(data)

def client_func(data):
    print(f"Message From Client : {data}")

c = PySock.client(
   client_name=  "shikhar",
   DSP_enable= True,
   file = r'client.yaml',
   debug = True,
   rememberServer = True
   )
c.CLIENT("localhost",1234)
c.CREATE_CHANNEL("test")
c.SEND(channel = "test", data = "Hello, World!")
c.HANDSHAKE(target_name= "swat")

count = 0
while run:

    if "swat" in c.HS_Devices:
        if count == 0:
            c.SEND_TO_CLIENT("swat","Hello From Shikhar")
            count += 1

    c.LISTEN("test",sample_func)

    c.LISTEN("DSP_MSG",client_func)

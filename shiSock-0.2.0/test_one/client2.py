import PySock

run = True

def sample_func(data):
    print(data)

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
while run:
    c.LISTEN("test",sample_func)

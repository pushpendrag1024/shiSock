import PySock

run = True

def sample_func(data):
    # global run
    print(data)
    # run = False

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
while run:
    c.LISTEN("test",sample_func)

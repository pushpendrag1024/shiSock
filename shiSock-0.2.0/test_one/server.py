import PySock

def sample_func(data,con):
        print(data)
        con.SEND("test",data["client_name"],"Hello From Server")

s = PySock.server(secure = True, file = r'server.yaml')
s.SERVER(address = "localhost", port = 1234, listeners = 10)
s.CREATE_CHANNEL("test")

while True:
        s.LISTEN(channel = "test", function = sample_func,args = (s,))

# C@C/piBsKTAP9?C
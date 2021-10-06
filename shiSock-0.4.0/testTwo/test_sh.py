from PySock import MAIN,SETUP

# SETUP()

def test_func(data):
    print(f"Data from client : {data}")

s = MAIN(address= "localhost",port = 1234, listeners = 1, timeout = 1)
    
print("Creating Channel")
s.CREATE_CHANNEL("test")

print("LISTENING")
while True:
    s.LISTEN("test", test_func)
from PySock import server,SetupIPC

SetupIPC()

# def test_func(data,con):
#     print(f"Data from client : {data}")
#     con.SEND(target = data["sender_name"], channel = data["type"], data = "Hello, What's up!")

# s = server(address = "localhost", port = 1234, listeners=1, timeout = 1)

# print("Creating Channel")
# s.CREATE_CHANNEL("test")

# print("LISTENING")
# while True:
#     s.LISTEN("test", test_func, s)


# import sys

# def main():
#     script = sys.argv[::]
#     print(script)


# if __name__ == '__main__':
#     main()
import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"Connecting to port {server_address}")
sock.connect(server_address)

time.sleep(1)

messages = [ 'Part one of the message.',
             'Part two of the message.',
             ]
amount_expected = len(''.join(messages))

try:

    # Send data
    for message in messages:
        print(f"Sending  : {message}")
        sock.sendall(bytes(message,"utf-8"))
        time.sleep(1.5)

    # Look for the response
    amount_received = 0
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"Received : {data}")

finally:
    print(f"Closing Socket")
    sock.close()
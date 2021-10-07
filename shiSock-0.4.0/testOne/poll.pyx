import select
import socket
import sys
import queue
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server_address = ('localhost', 10000)
print(f"[Starting Server On Port : {server_address}]")
server.bind(server_address)
server.listen(5)

message_queues = {}
TIMEOUT = 1000

FLAGS = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR | select.POLLOUT
poller = select.poll()
poller.register(server, FLAGS)

# Map file descriptors to socket objects
fd_to_socket = { server.fileno(): server,
               }

print('Waiting for the next event')
while True:
    #time.sleep(1)

    events = poller.poll(TIMEOUT)

    for fd, flag in events:

        s = fd_to_socket[fd]

         # Handle inputs
        if flag & (select.POLLIN | select.POLLPRI):

            if s is server:
                # A "readable" server socket is ready to accept a connection
                connection, client_address = s.accept()
                print(f"New Connection From : {client_address}")
                connection.setblocking(0)
                fd_to_socket[ connection.fileno() ] = connection
                poller.register(connection, FLAGS)

                # Give the connection a queue for data we want to send
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(1024)

                if data:
                    # A readable client socket has data
                    print(f"Received {data} from {s.getpeername()} ")
                    message_queues[s].put(data)
                    # Add output channel for response
                    # poller.modify(s, FLAGS)

                else:
                    # Interpret empty result as closed connection
                    print(f'closing "{client_address}" after reading no data')
                    # Stop listening for input on the connection
                    poller.unregister(s)
                    s.close()

                    # Remove message queue
                    del message_queues[s]

        elif flag & select.POLLHUP:
            # Client hung up
            print(f'closing "{client_address}" after receiving HUP')
            # Stop listening for input on the connection
            poller.unregister(s)
            s.close()

        elif flag & select.POLLOUT:
            # Socket is ready to send data, if there is any to send.
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                # No messages waiting so stop checking for writability.
                print(f"output queue for {s.getpeername()} is empty")
                # poller.modify(s, FLAGS)
            else:
                print(f"Sending {next_msg} to {s.getpeername()}")
                s.send(next_msg)

        elif flag & select.POLLERR:
            print(f"Handling exceptional condition for {s.getpeername()}")
            # Stop listening for input on the connection
            poller.unregister(s)
            s.close()

            # Remove message queue
            del message_queues[s]

        

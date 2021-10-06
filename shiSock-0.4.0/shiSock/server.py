import select
import socket
import base64
import pickle
import threading
import multiprocessing
import queue
from functools import lru_cache
import cProfile, pstats, io
import time

def profile(func):
    
    def  inner(*args, **kwargs):
        print(f"================================={func.__name__}================================")
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream = s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

class MAIN():

    def __init__(self,address : str, port : int, listeners : int, debug : bool = False) -> object:

        self.__debug : bool = debug

        self.__WRITABLE : list = []
        self.__INPUTS : list = []
        self.__OUTPUTS : list = []
        self.__USERNAME_QUEUE : dict = {}
        self.__CUSTOM__MESSAGE_HANDLER : dict = {}
        self.__SENDER_QUEUE = {}
        self.__SENDER_REQUEST : str = []
        self.conClients : str = []

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setblocking(False)

        self.sock.bind((address, port))
        self.sock.listen(listeners)

        if self.__debug:
            print("[SERVER IS ACTIVATED | LISTENING]")

        self.__INPUTS.append(self.sock)

        server_thread = threading.Thread(
            target = self.__server,
            args = ()
        )
        server_thread.daemon = True
        server_thread.start()
        
    def __remove_sock(self,sock):
        if self.__debug:
            print("User Disconnected")
        if sock in self.__OUTPUTS:
            self.__OUTPUTS.remove(sock)
        if sock in self.__WRITABLE:
            self.__WRITABLE.remove(sock)
        self.__INPUTS.remove(sock)
        sock.close()
        username = self.__USERNAME_QUEUE[sock]
        try:
            self.conClients.remove(username)
        except:
            pass

        del self.__USERNAME_QUEUE[sock]

    def __server(self):
        data_recv_len = []

        while True:
            readable, writable, exception = select.select(self.__INPUTS, self.__OUTPUTS, self.__INPUTS)

            for r in readable:

                if r is self.sock:
                    con,addr = r.accept()
                    con.setblocking(False)
                    self.__INPUTS.append(con)
                    self.__USERNAME_QUEUE[con] = "no_data"

                else:
                    ini = list(zip(*data_recv_len))
                    if len(ini) == 0 or r not in ini[0]:
                        try:
                            data_len = int(r.recv(32).decode().strip("-"))
                        except ConnectionResetError:
                            self.__remove_sock(r)
                            continue
                        except:
                            continue

                        if data_len:
                            data_recv_len.append([r,data_len])
                        else:
                            self.__remove_sock(r)
                            continue
                    else:
                        INDEX = ini[0].index(r)
                        try:
                            recv_len = data_recv_len.pop(INDEX)[1]
                            data = r.recv(recv_len)

                            data = pickle.loads(base64.b64decode(data))
                            # print(self.__USERNAME_QUEUE)
                            
                            try:
                                if self.__USERNAME_QUEUE[r] == "no_data":
                                    del self.__USERNAME_QUEUE[r]
                                    self.__USERNAME_QUEUE[data.strip("0")] = r
                                    self.conClients.append(data.strip("0"))
                                    self.__SENDER_QUEUE[data.strip("0")] = queue.Queue()
                                    if r not in self.__OUTPUTS:
                                        self.__OUTPUTS.append(r)
                            except KeyError:
                                if data["channel"] == "DSP_MSG":
                                    self.__SENDER_QUEUE[data["target_name"]].put(data)
                                    self.__SENDER_REQUEST.append(data["target_name"])
                                elif data["channel"] in self.__CUSTOM__MESSAGE_HANDLER:
                                    self.__CUSTOM__MESSAGE_HANDLER[data["channel"]].put(data)

                                if r not in self.__OUTPUTS:
                                    self.__OUTPUTS.append(r)
                            
                        except ConnectionResetError:
                            self.__remove_sock(r)
                            continue
                        except EOFError:
                            pass

            self.__sender(writable, self.__USERNAME_QUEUE)
                    
            for e in exception:
                self.__remove_sock(r)

    def __sender(self,__writable, usernameQueue):

        for username in self.__SENDER_REQUEST:
            try:
                con = usernameQueue[username]
            except KeyError:
                continue

            if con._closed and con.fileno() == -1:
                __writable.remove(con)
                continue

            try:
                msg = self.__SENDER_QUEUE[username].get_nowait()
                prepare_send = base64.b64encode(pickle.dumps(msg))
                con.send(str(len(prepare_send)).center(16,"|").encode("utf-8"))
                con.send(prepare_send)
                self.__SENDER_REQUEST.remove(username)
            except queue.Empty:
                continue
            except KeyError:
                continue

    

    def CREATE_CHANNEL(self,channels : str = None, multiple : bool = False):
        if multiple:
            if type(channels) is type([]):
                for channel in channels:
                    if channel not in self.__CUSTOM__MESSAGE_HANDLER:
                        self.__CUSTOM__MESSAGE_HANDLER[channel] = queue.Queue()
        else:
            if channels not in self.__CUSTOM__MESSAGE_HANDLER:
                self.__CUSTOM__MESSAGE_HANDLER[channels] = queue.Queue()


    def SEND(self,target_name, channel : str = None, data = None):
        if not channel:
            raise TypeError("SEND() missing 1 required positional argument: 'channel'")
        if not data:
            raise TypeError("SEND() missing 1 required positional argument: 'data'")

        lst = [ [1,2], {"a":1}, (1,2), {1,2,}, "a", 12, 0.45, b"bytes" ]
        allowed_lst= []
        for l in lst:
            allowed_lst.append(type(l))
        if type(data) in allowed_lst:
            if channel in self.__CUSTOM_CHANNEL:
                prepare_send = {
                    "channel" : channel,
                    "sender_name" : "SERVER",
                    "target_name" : target_name,
                    "data" : data
                }
                self.__SENDER_QUEUE[target_name].put(prepare_send)
                self.__SENDER_REQUEST.append(target_name)

        else:
            raise TypeError(f"{type(data)} is not allowed as a sendable data type for 'data'")

    # @profile
    def LISTEN(self,channel : str = None, function : object = None, args = None):

        if not channel:
            raise TypeError("LISTEN() missing 1 required positional argument: 'channel'")

        if channel not in self.__CUSTOM__MESSAGE_HANDLER:
            raise None

        try:
            p_data = self.__CUSTOM__MESSAGE_HANDLER[channel].get_nowait()
            # print(p_data)
            if not args:
                # self.__CALLBACK_LOOP.append([function,[p_data]])
                function(*[p_data])
            else:
                args = list(args)
                args.insert(0,p_data)
                # self.__CALLBACK_LOOP.append([function,[args]])
                function(*[args])

        except queue.Empty:
            pass

    # def __callback_loop(self,__callbackLst):
    #     while True:
    #         for i,func in enumerate(__callbackLst):
    #             __callbackLst.pop(i)
    #             func[0](*func[1])

            
class server():
    def __init__(self,address : str, port : int, listeners : int, debug : bool = False):
        __parent = MAIN(address, port, listeners, debug)
        self.CREATE_CHANNEL = __parent.CREATE_CHANNEL
        self.LISTEN = __parent.LISTEN
        self.SEND = __parent.SEND
        self.conClients = __parent.conClients

#unstable
import select
import socket
import base64
import pickle
import json
import threading

class __server():

    def __init__(self, address : str = "localhost", port : int = 1022, listeners : int = 10, debug : bool = False) -> None:
        '''This server is just for prototype and this should not be used in production.
        We are adding some new features in this file thats why please do not use in right now.'''

        self.debug = debug

        self.counter = 99999999
        self.__WRITABLE = []
        self.__INPUTS = []
        self.__OUTPUTS = []
        self.__MESSAGE_QUEUES = {}
        self.__IDENTIFIER = {}

    def _SERVER(self, Address : str, Port : int, Listeners : int) -> None:

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setblocking(False)

        self.sock.bind((Address, Port))
        self.sock.listen(Listeners)

        if self.debug:
            print("[SERVER IS ACTIVATED | LISTENING]")

        self.__INPUTS.append(self.sock)


    def __server(self):

        data_recv_len = []

        while True:

            readable, writable , exception = select.select(self.__INPUTS, self.__OUTPUTS, self.__INPUTS)

            for r in readable:

                if r is self.sock:
                    con, addr = r.accept()
                    con.setblocking(False)
                    self.counter -= 1
                    name = self.counter
                    self.__IDENTIFIER[name] = con
                    self.__MESSAGE_QUEUES[name] = {
                        "0.1.0" : base64.b64encode(json.dumps({"type":"code-new-0.1.0", "identifier" : f"{name}"}))
                    }

                else:

                    ini = list(zip(*data_recv_len))
                    if len(ini) == 0 or r not in ini[0]:
                        data_len = int(r.recv(32).decode().strip("-"))

                        if data_len:
                            data_recv_len.append([r,data_len])
                        else:
                            if self.debug:
                                print("User Disconnected")

                    else:
                        INDEX = ini[0].index(r)

                        buffer = data_recv_len.pop(INDEX)[1]
                        data = r.recv(buffer)
                        # data = json.loads(base64.b64decode(data))
                        self.__RECEIVING_MSG.append(data)
                        if r not in self.__OUTPUTS:
                            self.__OUTPUTS.append(r)
            
            for w in writable:
                if w not in self.__WRITABLE:
                    self.__WRITABLE.append(w)

            for e in exception:
                self.__INPUTS.remove(e)
                if e in self.__OUTPUTS:
                    self.__OUTPUTS.remove(e)
                del self.__MESSAGE_QUEUES[e]


    def _handler(self,):
        while True:
            for i,data in enumerate(self.__RECEIVING_MSG):
                resData = json.loads(base64.b64decode(data))
                if resData["channel"] == "DSP_MSG":
                    if resData["target_name"] in self.__MESSAGE_QUEUES:
                        self.__MESSAGE_QUEUES[resData["target_name"]].__setitem__("0.2.0", data)
                    else:
                        self.__MESSAGE_QUEUES[resData["target_name"]] = {
                            "0.2.0" : data
                        }
                    self.__RECEIVING_MSG.pop(i)
                elif resData["channel"] in self.__CUSTOM_CHANNEL:
                    self.__MESSAGE_HANDLER.append(resData)
                    self.__RECEIVING_MSG.pop(i)


    def _sender(self):
        while True:

            queueValue = self.__MESSAGE_QUEUES.values()
            queueKey = self.__MESSAGE_QUEUES.keys()

            for i,ky in enumerate(queueKey):

                try:
                    sock = self.__IDENTIFIER[ky]
                except KeyError:
                    continue
                
                if sock in self.__WRITABLE:
                    dictData = queueValue[i]
                    if "0.1.0" in dictData.keys():
                        data = dictData["0.1.0"]
                        sock.send(data)
                        dictData.pop("0.1.0")
                    dDKeys = dictData.keys()
                    for index,data in enumerate(dictData.values()):
                        sock.send(data)
                        key = dDKeys[index]
                        dictData.pop(key)

                    


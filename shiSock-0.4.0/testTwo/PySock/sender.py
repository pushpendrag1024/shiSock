import json
import base64
import select
import socket
import os
import sys
import multiprocessing
from subprocess import call as executeSH
from subprocess import run,Popen
import shutil
import random

class SETUP():
    def __init__(self):

        self.Base_Dir = __file__
        self.CWD = os.getcwd()

        print(self.Base_Dir)

        try:
            p_name = sys.platform

            print(f"platform : {p_name}")

            if p_name == 'win32':
                self.for_windows()
            elif p_name == 'linux':
                self.for_linux()
            elif p_name == 'mac':
                self.for_mac()
                
        except Exception as e:
            print(e)

    def name_generator(self,_len_ = 16, onlyText = False):
        lower_case = list("abcdefghijklmnopqrstuvwxyz")
        upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        special = list("!@#$%&*?")
        number = list("0123456789")

        if onlyText:
            _all_ = lower_case + upper_case
        else:
            _all_ = lower_case + upper_case + special + number
            
        random.shuffle(_all_)
        return "".join(random.sample(_all_,_len_))

    def for_linux(self):

        def write_file(__password):
            lines = [
                "import redis\n"
                "import sys\n"
                "class varify():\n"
                "   def __init__(self):\n"
                f"       self.ascaec = '{__password}'\n"
                "       self.PORT = 2210\n"
                "       self.HOST = u'localhost'\n"
                        
                "   def authenticate(self):\n"
                "       try:\n"
                "           r = redis.Redis(host = self.HOST, port = self.PORT, password = self.ascaec)\n"
                "           return r\n"
                "       except redis.AuthenticationError:\n"
                "           print('Something Went Wrong, Try again!')\n"
                "           sys.exit(1)\n"
            ]

            f = open(file = "varify.pyx", mode = "w+")
            f.writelines(lines)

        path_lst = self.Base_Dir.split("/")
        path_lst.pop()
        path_lst.append("setup.sh")

        setup_path = "/".join(path_lst)

        print(f"setup path : {setup_path}")

        executeSH(setup_path)
        files = os.popen("ls").read().split("\n")
        print(files)
        for file in files:
            if file.endswith(".tar.gz"):
                os.remove(f"{self.CWD}/{file}")
        print(files)
        sfcewsvevw = self.name_generator(_len_ = 42)
        print("writing file")
        write_file(sfcewsvevw)

        lines = [
            "from setuptools import Extension, setup\n"
            "from Cython.Build import cythonize\n"
            "ext_modules = [\n"
            "    Extension(\n"
            '        "varify",\n'
            '        ["varify.pyx"],\n'
            "        extra_compile_args=['-fopenmp'],\n"
            "        extra_link_args=['-fopenmp'],\n"
            "    )\n"
            "]\n"

            "setup(\n"
                "name='auth',\n"
                "ext_modules=cythonize(ext_modules),\n"
            ")\n"
        ]

        f = open(file = r"setup.py", mode = "w+")
        f.writelines(lines)
        f.close()

        executeSH("ls")

        run(args = ("python3", "setup.py", "build_ext", "--inplace"))



        read_data = open(file = r'redis-6.2.5/redis.conf', mode = "r")
        data = read_data.read().split("\n")
        s = []

        for l in data:
            if l.startswith("#"):
                pass
            elif l.startswith("port"):
                prt = l.split(" ")
                prt.pop()
                prt.append("2210")
                s.append("".join(prt))
            else:
                if len(l) > 0:
                    s.append(l)
                    s.append("\n")

        s.append(f"requirepass {sfcewsvevw}")

        new_file = open(file = r"redis-6.2.5/PySock_redis.conf", mode = "w+")
        new_file.writelines(s)

        read_data.close()
        new_file.close()

        

        os.remove(r"redis-6.2.5/redis.conf")
        os.remove(r"varify.pyx")
        os.remove(r"varify.c")
        shutil.rmtree(r"build")
        os.remove(r"setup.py")

        print("===============================Done================================")
        sys.exit(0)

    def for_windows(self):
        pass

    def for_mac(self):
        pass

try:
    from varify import varify
except:
    print("Setup for ipc is not yet done, please complete the setup. Would you like to setup the ipc right now", end = " ")
    inp = input("(y/n) : ").lower()
    print()

    if inp == "y":
        SETUP()
    else:
        sys.exit()
    sys.exit(0)

class MAIN(varify):

    def __init__(self,address: str,port : int, listeners : int, timeout : int):

        varify.__init__(self)

        try:
            Popen(args = ("redis-6.2.5/src/redis-server", "redis-6.2.5/PySock_redis.conf"))
        except FileNotFoundError as e:

            print(e)

        print(f"__init__ pid : {os.getpid()}")

        print("Starting Process.....")
        
        main_server_process = multiprocessing.Process(
            target = self.__server,
            args = (address,port,listeners,timeout)
        )

        controller_process = multiprocessing.Process(
            target = self.__controller,
        )

        main_server_process.start()
        controller_process.start()
        print("Process Started.......")

        self.IPC = self.authenticate()


        # p_name = sys.platform
        # print(f"=====================p_name = {p_name}=====================")
        # if p_name == "linux":
        #     run("clear")


    def __server(self, address : str, port : int, listeners : int, timeout : int) -> None:

        print("Server Process Started")
        print(f"server pid : {os.getpid()}")

        ipc = self.authenticate()

        serSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serSock.setblocking(False)
        serSock.bind((address, port))
        serSock.listen(listeners)

        FLAGS = select.POLLIN | select.POLLPRI | select.EPOLLHUP | select.EPOLLERR | select.POLLOUT
        poller = select.poll()
        poller.register(serSock,FLAGS)

        fd_to_socket = {serSock.fileno() : serSock,}
        data_len_dict = {}

        while True:

            events = poller.poll(timeout)
            for fd, flag in events:

                sock = fd_to_socket[fd]
                if flag & (select.POLLIN | select.POLLPRI):
                    if sock is serSock:
                        connection, client_addr = sock.accept()
                        connection.setblocking(False)
                        fd_to_socket[connection.fileno()] = connection
                        poller.register(connection, FLAGS)
                    else:
                        try:
                            data_len = data_len_dict[sock.getpeername()]
                            del data_len_dict[sock.getpeername()]
                            data = sock.recv(data_len)
                            if data:
                                ipc.rpush("data", json.dumps([fd,data]) )
                            else:
                                sock.close()
                                pass
                        except KeyError:
                            data_len = sock.recv(32)
                            if data_len:
                                data_len = data_len.decode().strip("`")
                                data_len_dict[sock.getpeername()] = int(data_len)

                elif flag and select.POLLOUT:

                    username = ipc.hget(name = "fd_names_store", key = int(fd))
                    data_lst = ipc.hget(name = "sender_queue", key = username)

                    for Data in data_lst:
                        sock.send( bytes( f"{len(Data)}".center(32,"`") , "utf-8" ) )
                        sock.send(Data)


    def __controller(self):

        print("Controller Process Started")
        print(f"__controller pid : {os.getpid()}")

        ipc = self.authenticate()

        while True:

            raw_data = ipc.rpop(name = "sender_queue")

            if raw_data is not None:

                all_data = json.loads(raw_data)
                fd = all_data[0]
                data = all_data[1]

                SACN_names = ipc.hvals("fd_names_store")

                if data["type"] == "code-0.0.1-new":
                    # data = {"type" : "code-0.0.1-new", "sender_name" : "client_name"}
                    if bytes(data["sender_name"],"utf-8") not in SACN_names:
                        g_name = bytes(data["sender_name"],"utf-8")
                        OBJECT = {"type" : "code-0.0.2-new", "sender_name" : "SERVER", "target_name" : int(fd),"data" : g_name }
                        sendable_object = base64.b64encode(json.dumps(OBJECT))
                        ipc.hsetnx(name = "fd_names_store", key = int(fd), value = g_name)
                        ipc.hset(name = "sender_queue", key = g_name, value = json.dumps([sendable_object]))
                        
                    else:
                        name = ""
                        count = 1
                        while True:
                            g_name = bytes(data["sender_name"] + "_" + f"{count}", "utf-8")
                            if g_name not in SACN_names:
                                OBJECT = {"type" : "code-0.0.2-new", "sender_name" : "SERVER", "target_name" : int(fd),"data" : g_name}
                                sendable_object = base64.b64encode(json.dumps(OBJECT))
                                ipc.hsetnx(name = "fd_names_store", key = int(fd), value = g_name)
                                ipc.hset(name = "sender_queue", key = g_name, value = json.dumps([sendable_object]))
                                break
                            count += 1

                elif data["type"] == "DSP_MSG":
                    # data = {"type" : "DSP_MSG", "sender_name" : "SACN sender name", "target_name" : "SACN target name", "data" : "xyzzzsdcdv"}
                    
                    if data["target_name"] in ipc.hkeys(name = "sender_queue"):
                        data_to_q = ipc.hget(name = "sender_queue", key = data["target_name"])
                        data_to_q.append(base64.b64encode(raw_data))
                        ipc.hset(name = "sender_queue", key = data["target_name"], value = data_to_q)
 
                elif data["type"] in ipc.lrange(name = "custome_channels", start = 0, end = -1):
                    # data =  {"type" : "channels_names", "sender_name" : "SACN sender name", "target_name" : "SACN target name", "data" : "sdcsdvsdvsdvsd"}
                    channel_lst = ipc.hget(name = "channels", key = data["type"])
                    channel_lst.append(raw_data)
                    ipc.hset(name = "channels",key = data["type"], value = channel_lst)

    def CREATE_CHANNEL(self, channel : str, multiple : bool = False) -> bool:

        channel_lst = self.IPC.lrange(name = "channels", start = 0, end = -1)

        if multiple:
            if type(channel) is type([]):
                for CHANNEL in channel:
                    if bytes(CHANNEL,"utf-8") not in channel_lst:
                        channel_lst.append(bytes(CHANNEL,"utf-8"))
                        self.IPC.hset(name = "channels", key = CHANNEL, value = json.dumps([]))
                return True
            else:
                pass
                # need to raise an error=================================
        else:
            if channel not in channel_lst:
                self.IPC.hset(name = "channels" ,key = channel, value = json.dumps([]))
                return True
            else:
                return False

    def SEND(self, target : str, channel : str, data : any) -> None:

        channel_lst = self.IPC.lrange(name = "channels", start = 0, end = -1)

        lst = [ [1,2], {"a":1}, (1,2), {1,2,}, "a", 12, 0.45, b"bytes" ]
        allowed_lst= []

        for l in lst:
            allowed_lst.append(type(l))

        if type(data) in allowed_lst:
            if channel in channel_lst:

                prepare_send = {
                    "type" : channel,
                    "sender_name" : "SERVER",
                    "target_name" : target,
                    "data" : data
                }

                json_data = json.dumps(prepare_send)
                b64_data = base64.b64encode(json_data)

                self.IPC.hset(name = "sender_queue", key = target, value = b64_data)
            else:
                # need a raise a custom error =================================================================
                pass
        else:
            raise TypeError(f"{type(data)} is not allowed as a transmitable data type for argument 'data'")

    def LISTEN(self,channel : str, function : object, args : any = None) -> None:

        channel_lst = self.IPC.lrange(name = "channels", start = 0, end = -1)
        
        if channel in channel_lst:
            
            json_data = self.IPC.hget(name = "channels", key = channel)
            data_lst = json.loads(json_data)
            if len(data_lst) > 0:
                for data in data_lst:
                    if not args:
                        function(*[data])
                        data_lst.remove(data)
                    else:
                        args = list(args)
                        args.insert(0,data)
                        function(*[args])
                        data_lst.remove(data)

                        

# def test_func(data):
#     print(f"Data from client : {data}")
    
# s = MAIN(address = "localhost", port = 1234, listeners = 100, timeout = 1)
# print("Creating Channel")
# s.CREATE_CHANNEL("test")

# print("LISTENING")
# while True:
#     s.LISTEN("test", test_func)

# s = __setup_()


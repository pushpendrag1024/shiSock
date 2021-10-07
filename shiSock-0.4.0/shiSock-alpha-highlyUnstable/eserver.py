import json
import base64
import select
import socket
import os
import sys
import multiprocessing
from subprocess import call as executeSH
from subprocess import run,Popen
import subprocess as sp
import shutil
import random
from rich import print as rprint

class SetupIPC():
    def __init__(self):

        self.Base_Dir = __file__.split("/")
        self.Base_Dir.pop()
        self.Base_Dir = "/".join(self.Base_Dir)
        self.CWD = os.getcwd()
        
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

        os.remove(r"varify.pyx")
        os.remove(r"varify.c")
        shutil.rmtree(r"build")
        os.remove(r"setup.py")

        result = run("ls",stdout = sp.PIPE)
        result = result.stdout
        result = result.decode().split("\n")
        print(f"result : {result}")
        for f in result:
            if f.endswith(".so"):
                run(args = ("mv", f"{self.CWD}/{f}", f"{self.CWD}/py-sock"))
                break

        os.mkdir("build")
        os.mkdir("build/src")

        f = open(file = f"{self.Base_Dir}/src/sample.conf", mode = "r")
        q = f.read()
        q = q.split("\n")
        q.append(f"requirepass {sfcewsvevw}")

        f2 = open(file = f"{self.CWD}/build/pysock.conf", mode = "w+")
        for line in q:
            f2.write(line+"\n")

        shutil.copy(f"{self.Base_Dir}/src/redis-server", f"{self.CWD}/build/src")

        print("===============================Done================================")
        sys.exit(0)

    def for_windows(self):
        pass

    def for_mac(self):
        pass

class Verify():

    def __init__(self):
        try:
            from varify import varify
            varify.__init__(self)
        except ImportError:
            rprint("[red]No IPC setup found")
            rprint("[yellow]You can setup the IPC using command: [green]{ python -m shisock --setupIPC }[yellow] from your current working directory.")
            sys.exit(0)


class serverLinux(Verify):

    def __init__(self,address: str,port : int, listeners : int, timeout : int):

        Verify.__init__(self)

        try:
            Popen(args = ("build/src/redis-server", "build/pysock.conf"))
        except FileNotFoundError as e:
            print(e)

        t = True
        while t:
            try:
                r = self.authenticate()
                if r.ping() == True:
                    t = False
                    r.connection_pool.disconnect()
            except Exception as e:
                print(e)
        
        main_server_process = multiprocessing.Process(
            target = self.__server,
            args = (address,port,listeners,timeout)
        )

        controller_process = multiprocessing.Process(
            target = self.__controller,
        )

        main_server_process.start()
        controller_process.start()

        self.IPC = self.authenticate()

        p_name = sys.platform
        if p_name == "linux":
            run("clear")
        print("[SERVER IS ACTIVATED | LISTENING]")


    def __server(self, address : str, port : int, listeners : int, timeout : int) -> None:

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
                            data = data.decode()
                            if data:
                                ipc.rpush("recieve_data", json.dumps([fd,data]) )
                            else:
                                sock.close()
                                ipc.hdel('fd_names_store', int(fd))
                                rprint(f"[red]Connection CLosed")
                            
                        except KeyError:
                            data_len = sock.recv(32)
                            if data_len:
                                data_len = data_len.decode().strip("`")
                                data_len_dict[sock.getpeername()] = int(data_len)
                            else:
                                sock.close()
                                ipc.hdel('fd_names_store', int(fd))
                                rprint(f"[red]Connection CLosed")

                elif flag and select.POLLOUT:

                    username = ipc.hget(name = "fd_names_store", key = int(fd))
                    if username is not None:
                        for _ in range(ipc.llen(f"stream{username.decode()}")):
                            Rdata = ipc.rpop(f"stream{username.decode()}")

                            sock.send( bytes( f"{len(Rdata)}".center(32,"`") , "utf-8" ) )
                            sock.send(Rdata)
                                

    def __controller(self):

        ipc = self.authenticate()

        while True:

            raw_data = ipc.rpop(name = "recieve_data")
            reserve = raw_data
            if raw_data is not None:

                raw_data = raw_data.decode()

                all_data = json.loads(raw_data)
                fd = all_data[0]
                data = json.loads(all_data[1])

                SACN_names = ipc.lrange(name = "hsDevices", start = 0, end = -1)

                if data["type"] == "code-0.0.1-new":
                    SENDER_NAME = bytes(data["sender_name"], "utf-8")
                    if SENDER_NAME not in SACN_names:
                        g_name = data["sender_name"]
                        
                        OBJECT = {"type" : "code-0.0.2-new", "sender_name" : "SERVER", "target_name" : g_name,"data" : g_name }
                        sendable_object = base64.b64encode(bytes(json.dumps(OBJECT) , "utf-8" )).decode()

                        ipc.lpush("hsDevices", g_name)
                        ipc.lpush(f"stream{g_name}",sendable_object)
                        ipc.hsetnx(name = "fd_names_store", key = int(fd), value = g_name)

                    else:
                        count = 1
                        t = True
                        while t:

                            g_name = SENDER_NAME + bytes(f"_{count}", "utf-8")
                            if g_name not in SACN_names:

                                g_name = g_name.decode()

                                OBJECT = {"type" : "code-0.0.2-new", "sender_name" : "SERVER", "target_name" : g_name,"data" : g_name}
                                sendable_object = base64.b64encode(bytes(json.dumps(OBJECT) , "utf-8" )).decode()

                                ipc.lpush("hsDevices", g_name)
                                ipc.lpush(f"stream{g_name}",sendable_object)
                                ipc.hsetnx(name = "fd_names_store", key = int(fd), value = g_name)
                                t = False
                            count += 1

                elif data["type"] == "DSP_MSG":

                    if bytes(data["target_name"] , "utf-8") in ipc.lrange(name = "hsDevices" , start = 0, end = -1):

                        d_data = json.dumps(data)
                        bd_data = base64.b64encode(bytes(d_data, "utf-8")).decode()

                        ipc.lpush(f"stream{data['target_name']}" , bd_data)
                    else:
                        ipc.lpush("recieve_data", reserve)
                            

                elif bytes(data["type"], "utf-8") in ipc.lrange(name = "custome_channels", start = 0, end = -1):
                    if bytes( data["sender_name"] , "utf-8") in ipc.lrange(name = "hsDevices", start = 0, end = -1):
                        # data =  {"type" : "channels_names", "sender_name" : "SACN sender name", "target_name" : "SACN target name", "data" : "sdcsdvsdvsdvsd"}
                        channel_lst = ipc.hget(name = "channels", key = data["type"])
                        if channel_lst is not None:
                            channel_lst = json.loads(channel_lst)
                            channel_lst.append(data)
                            channel_lst = json.dumps(channel_lst)
                            ipc.hset(name = "channels",key = data["type"], value = channel_lst)
                    else:
                        print(f"Not a HS device : {data['sender_name']}")


    def CREATE_CHANNEL(self, channel : str, multiple : bool = False) -> bool:

        channel_lst = self.IPC.lrange(name = "custome_channels", start = 0, end = -1)

        if multiple:
            if type(channel) is type([]):
                for CHANNEL in channel:
                    if bytes(CHANNEL,"utf-8") not in channel_lst:
                        channel_lst.append(bytes(CHANNEL,"utf-8"))
                        self.IPC.hset(name = "channels", key = CHANNEL, value = json.dumps([]))
                        self.IPC.lpush("custome_channels", channel)
                return True
            else:
                pass
        else:
            if channel not in channel_lst:
                self.IPC.hset(name = "channels" ,key = channel, value = json.dumps([]))
                self.IPC.lpush("custome_channels", channel)
                return True
            else:
                return False

    def SEND(self, target : str, channel : str, data : any) -> None:

        channel_lst = self.IPC.lrange(name = "custome_channels", start = 0, end = -1)

        lst = [ [1,2], {"a":1}, (1,2), {1,2,}, "a", 12, 0.45, b"bytes" ]
        allowed_lst= []

        for l in lst:
            allowed_lst.append(type(l))

        if type(data) in allowed_lst:
            if bytes(channel, "utf-8") in channel_lst:

                prepare_send = {
                    "type" : channel,
                    "sender_name" : "SERVER",
                    "target_name" : target,
                    "data" : data
                }

                json_data = json.dumps(prepare_send)
                b64_data = base64.b64encode(bytes(json_data , "utf-8")).decode()

                self.IPC.lpush(f"stream{target}" , b64_data)

            else:
                pass
        else:
            raise TypeError(f"{type(data)} is not allowed as a transmitable data type for argument 'data'")

    def LISTEN(self,channel : str, function : object, *args : any) -> None:

        channel_lst = self.IPC.hget(name = "channels", key = channel)

        if channel_lst is not None:
            
            json_data = channel_lst
            
            data_lst = json.loads(json_data)
            if len(data_lst) > 0:
                for data in data_lst:
                    if not args:
                        function(*[data])
                        data_lst.remove(data)
                    else:
                        args = list(args)
                        args.insert(0,data)
                        function(*args)
                        data_lst.remove(data)

                data_lst = json.dumps(data_lst)
                self.IPC.hset(name = "channels" ,key = channel, value = data_lst)



class eserver():
    def __init__(self,secure = False, DSP_enable=False, file = None, debug = False, MTCL : bool = True, MPCL : bool = None):

        try:
            p_name = sys.platform

            if p_name == 'linux':
                __parent = serverLinux(secure,DSP_enable,file,debug,MTCL,MPCL)
            elif p_name == 'mac':
                __parent = serverLinux(secure,DSP_enable,file,debug,MTCL,MPCL)

            self.Server = __parent.SERVER
            self.CreateChannel = __parent.CREATE_CHANNEL
            self.LISTEN = __parent.LISTEN
            self.Send = __parent.SEND
            self.conClients = __parent.conClients


        except Exception as e:
            print(e)
            sys.exit(0)
                
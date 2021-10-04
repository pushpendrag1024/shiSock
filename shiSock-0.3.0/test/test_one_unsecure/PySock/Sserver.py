import pickle
import socket
from random import sample, shuffle

urandom = pickle.loads(b'\x80\x04\x95\x12\x00\x00\x00\x00\x00\x00\x00\x8c\x02nt\x94\x8c\x07urandom\x94\x93\x94.')
mThread = pickle.loads(b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00\x8c\tthreading\x94\x8c\x06Thread\x94\x93\x94.') # done
yaml_dump = pickle.loads(b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00\x8c\x04yaml\x94\x8c\x04dump\x94\x93\x94.') # done
yaml_full_load = pickle.loads(b'\x80\x04\x95\x16\x00\x00\x00\x00\x00\x00\x00\x8c\x04yaml\x94\x8c\tfull_load\x94\x93\x94.') # done
default_backend = pickle.loads(b'\x80\x04\x954\x00\x00\x00\x00\x00\x00\x00\x8c\x1ccryptography.hazmat.backends\x94\x8c\x0fdefault_backend\x94\x93\x94.')
AESGCM = pickle.loads(b'\x80\x04\x95:\x00\x00\x00\x00\x00\x00\x00\x8c+cryptography.hazmat.primitives.ciphers.aead\x94\x8c\x06AESGCM\x94\x93\x94.')
load_ssh_public_key = pickle.loads(b'\x80\x04\x95L\x00\x00\x00\x00\x00\x00\x00\x8c0cryptography.hazmat.primitives.serialization.ssh\x94\x8c\x13load_ssh_public_key\x94\x93\x94.')
SHA256 = pickle.loads(b'\x80\x04\x954\x00\x00\x00\x00\x00\x00\x00\x8c%cryptography.hazmat.primitives.hashes\x94\x8c\x06SHA256\x94\x93\x94.')
OAEP = pickle.loads(b'\x80\x04\x95>\x00\x00\x00\x00\x00\x00\x00\x8c1cryptography.hazmat.primitives.asymmetric.padding\x94\x8c\x04OAEP\x94\x93\x94.')
MGF1 = pickle.loads(b'\x80\x04\x95>\x00\x00\x00\x00\x00\x00\x00\x8c1cryptography.hazmat.primitives.asymmetric.padding\x94\x8c\x04MGF1\x94\x93\x94.')
b64encode = pickle.loads(b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00\x8c\x06base64\x94\x8c\tb64encode\x94\x93\x94.')
b64decode = pickle.loads(b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00\x8c\x06base64\x94\x8c\tb64decode\x94\x93\x94.')
select = pickle.loads(b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c\x06select\x94\x8c\x06select\x94\x93\x94.')
mProcess = pickle.loads(b"\x80\x04\x95'\x00\x00\x00\x00\x00\x00\x00\x8c\x17multiprocessing.context\x94\x8c\x07Process\x94\x93\x94.")

encoding_one = "utf-8"

class IPNC():

    def __init__(self):
        pass

    def read_yml(self,file = None):

        with open(file) as file:
            documents = yaml_full_load(file)
            return documents

    def write_yml(self,file = None, dict_data = None,mode = "a+"):

        with open(file, mode) as file:
            yaml_dump(dict_data, file)

    def add_node(self,file = None, node = None):
        try:
            read = self.read_yml(file)
            if read != None:
                read[node[0]]
                self.change_node_value(file,node)
            else:
                raise KeyError
        except KeyError:
            node_dict = {
                node[0] : node[1]
            }
            self.write_yml(file, node_dict)

    def change_node_value(self,file = None, node = None):
        r_yml = self.read_yml(file)
        r_yml[node[0]] = node[1]
        self.write_yml(file = file, dict_data = r_yml, mode = "w")

    def get_node(self,file = None, key = None, wait = True):
        if key == None:
            return self.read_yml(file)
        
        if wait:
            while True:
                r_yml = self.read_yml(file)
                try:
                    value = r_yml[key]
                    return value
                except KeyError:
                    pass

                except TypeError:
                    pass
        else:
            r_yml = self.read_yml(file)
            try:
                value = r_yml[key]
                return value
            except KeyError:
                return None

            except TypeError:
                pass

    def name_generator(self,_len_ = 16, onlyText = False):
        lower_case = list("abcdefghijklmnopqrstuvwxyz")
        upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        special = list("!@#$%&*?")
        number = list("0123456789")

        if onlyText:
            _all_ = lower_case + upper_case
        else:
            _all_ = lower_case + upper_case + special + number
            
        shuffle(_all_)
        return "".join(sample(_all_,_len_))

    def code001_AN(self,file = None, key = None ,target_key = None, value = None):
        read = self.get_node(
            file = file,
            key = key,
            wait = False
        )

        if read is not None:
            read[target_key] = value

            self.add_node(
                file = file,
                node = [
                    key,
                    read
                ]
            )
        else:
            self.add_node(
                file = file,
                node = [
                    key,
                    {target_key : value}
                ]
            )
        
    def code001_UN(self,file = None, key = None, target_key = None, position : int = None, value = None):
        read = self.get_node(
            file = file,
            key = key,
            wait = False
        )
        if read is not None:

            if position == None:
                read[target_key] = value
            else:
                base = read[target_key]
                base.pop(position)
                base.insert(position,value)
                read[target_key] = base

            self.add_node(
                file = file,
                node = [
                    key,
                    read
                ]
            )

class DspError(Exception):
    def __init__(self,err_msg):
        print(err_msg)

class MAIN(IPNC):

    def __init__(self, file = None, debug : bool = False, MTCL : bool = True, MPCL : bool = False, safeMode : bool = True):

        self.__KEY = b',p\xe1+z\x06F\xf9"y\xf4\'\xc7\xb3\x8es4\xd8\xe58\x9c\xff\x16z\x1d\xc3\x0es\xf8&\xb6\x83'
        self.__SECURE = "secure"   
        self.__SENDER_NAME = "sender_name" 
        self.__AES_KEY = "aes_key"
        self.__NONCE = "nonce" 
        self.__DATA = "data"    
        self.__AAD = "aad" 
        self.__TARGET_NAME = "target_name"  
        self.__SERVER = b64encode(pickle.dumps("server"))
        self.__NO_DATA = b'\xef=\x99\xbaN|\x0e\xfd\x85i\x1e\xfd\xe5,\x05\x0b!\xf0&\xff\xa7\x1f\xd9+\xc6+Kc\xd2\x18\xcb\xb4'
        self.__TYPE = "type"   
        self.__CODE_100_NEW = "code-1.0.0-new" 
        self.__CODE_110_NEW = "code-1.1.0-new" 
        self.__CODE_111_NEW = "code-1.1.1-new"    
        self.__DSP_REQ = "DSP_REQ"     
        self.__DSP_HR_L1 = "DSP_HR_L1"    
        self.__DSP_HR_L2 = "DSP_HR_L2"    
        self.__DSP_MSG = "DSP_MSG"   
        self.__USERNAME = "username"  
        self.__VARIFIED = "varified"  
        self.__UNVARIFIED = "unvarified" 
        self.__SAVE = b'\x15}\xca\x92\xe4%\x04X3\x9dK\x83RP\xd4L#\x8f3U\xe1\xb7\x98a\x95\x18\x8e\xe44\xe9\xba\xff'

        IPNC.__init__(self)
        self.__debug = debug

        if MPCL and MTCL:
            raise ValueError("both 'MPCL' abd 'MTCL' should not be set to True")

        elif not MPCL and not MTCL:
            raise ValueError("both 'MPCL' abd 'MTCL' should not be set to False")

        else:
            self.__MPCL = MPCL
            self.__MTCL = MTCL

        if not file:
                raise TypeError("__init__() missing 1 required positional argument: 'file'")

        self.__file_location = file

        self.__WRITABLE = []
        self.__INPUTS = []
        self.__OUTPUTS = []
        self.__MESSAGE_QUEUES = {}
        self.__CUSTOM_CHANNEL = []
        self.__CALLBACK_LOOP = []
        self.__RECEIVING_MSG = []
        self.__MESSAGE_HANDLER = []
        self.__SENDER_QUEUE = []
        self.__KEY_STORE = {}
        self.conClients = []
        self.VARIFIED_DEVICES = []

        if safeMode:

            __code003_hs_dict = self.get_node(
                file = self.__file_location,
                key = self.__KEY,
                wait = False
            )

            if __code003_hs_dict is not None:
                self.__KEY_STORE = __code003_hs_dict



                self.VARIFIED_DEVICES.extend(list(__code003_hs_dict.keys()))



    def __load_object(self, data = None, secure : bool = True, key_dict : bytes = None):
        if not data:
            raise TypeError("__load_object() missing one positional argument 'data'")
        if secure:
            if not key_dict:
                raise TypeError("__load_object() missing one positional argument 'key_dict', it is compulsory when secure is set to True")
            else:
                pass

        loaded = pickle.loads(b64decode(data))

        if loaded[self.__SECURE] and secure:

            key_pack = pickle.loads(b64decode(key_dict[loaded[self.__SENDER_NAME]][1]))

            aes_gcm = AESGCM(key_pack[self.__AES_KEY])
            decryptedtext = aes_gcm.decrypt(
                nonce = key_pack[self.__NONCE],
                data = loaded[self.__DATA],
                associated_data = key_pack[self.__AAD]
            )

            unflatted = pickle.loads(b64decode(decryptedtext))

            return unflatted

        elif not secure and not loaded[self.__SECURE]:

            unflatted = pickle.loads(b64decode(loaded[self.__DATA]))

            return unflatted

    def __serializer(self, object = None, secure : bool = True, key_dict : bytes = None):

        if not object:
            raise TypeError("__load_object() missing one positional argument 'data'")
        else:
            if type(object) != type({1:"a"}):
                raise TypeError(f"__serializer() 'object' argument should be of type {type({'a':1})}")
        if secure:
            if not key_dict:
                raise TypeError("__load_object() missing one positional argument 'key_dict', it is compulsory when secure is set to True")

        normalize = b64encode(pickle.dumps(object))

        if secure:

            target = object[self.__TARGET_NAME]
            key_pack = pickle.loads(b64decode(key_dict[target][1]))

            aes_gcm = AESGCM(key_pack[self.__AES_KEY])
            cyphertext = aes_gcm.encrypt(
                nonce = key_pack[self.__NONCE],
                data = normalize,
                associated_data = key_pack[self.__AAD]
            )

            prepare_serialized_data = {self.__SECURE : secure, self.__SENDER_NAME : self.__SERVER, self.__DATA : cyphertext}
            flatten_psd = b64encode(pickle.dumps(prepare_serialized_data))

            return flatten_psd
        else:

            prepare_serialized_data = {self.__SECURE : secure, self.__SENDER_NAME : self.__SERVER, self.__DATA : normalize}
            flatten_psd = b64encode(pickle.dumps(prepare_serialized_data))

            return flatten_psd

    def SERVER(self,address : str = None, port : int = None, listeners : int = None):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setblocking(False)

        self.sock.bind((address, port))
        self.sock.listen(listeners)

        if self.__debug:
            print("[SERVER IS ACTIVATED | LISTENING]")

        self.__INPUTS.append(self.sock)

        server_thread = mThread(
            target= self.__server,
            )

        receiver_thread = mThread(
            target= self.__handler,
            args = (
                self.__RECEIVING_MSG,
                self.VARIFIED_DEVICES
            ) 
        )

        sender_thread = mThread(
            target = self.__sender,
            args = (
                self.__WRITABLE,
                self.__SENDER_QUEUE
            )
        )

        if self.__MTCL:
            callback_loop_P_T = mThread(
                target = self.__callback,
                args = (self.__CALLBACK_LOOP,)
            )
        elif self.__MPCL:
            callback_loop_P_T = mProcess(
                target = self.__callback,
                args = (self.__CALLBACK_LOOP,)
            )

        server_thread.daemon = True
        receiver_thread.daemon = True
        sender_thread.daemon = True
        callback_loop_P_T.daemon = True

        server_thread.start()
        receiver_thread.start()
        sender_thread.start()
        callback_loop_P_T.start()

    def __server(self):
        data_recv_len = []

        while True:
            readable, writable, exception = select(self.__INPUTS, self.__OUTPUTS, self.__INPUTS)

            for r in readable:

                if r is self.sock:

                    con,addr = r.accept()
                    con.setblocking(False)
                    self.__INPUTS.append(con)
                    self.__MESSAGE_QUEUES[con] = self.__NO_DATA

                else:

                    ini = list(zip(*data_recv_len))
                    if len(ini) == 0 or r not in ini[0]:

                        try:
                            d = r.recv(16)
                            data_len = int(d.decode().strip("|"))

                        except ConnectionResetError:
                            self.__remove_sock(r)
                            continue

                        except ValueError:
                            self.__remove_sock(r)
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
                            if self.__MESSAGE_QUEUES[r] == self.__NO_DATA:
                                r_data = pickle.loads(b64decode(data))
                                self.__MESSAGE_QUEUES[r] = r_data[self.__SENDER_NAME]
                                self.conClients.append(r_data[self.__SENDER_NAME])
                                if r not in self.__OUTPUTS:
                                    self.__OUTPUTS.append(r)
                                self.__RECEIVING_MSG.append(data)
                            else:
                                self.__RECEIVING_MSG.append(data)
                                if r not in self.__OUTPUTS:
                                    self.__OUTPUTS.append(r)
                        except ConnectionResetError:
                            self.__remove_sock(r)
                            continue
            
            for w in writable:
                if w not in self.__WRITABLE:
                    self.__WRITABLE.append(w)

            for e in exception:
                self.__remove_sock(e)
            
    def __remove_sock(self,sock):
        if self.__debug:
            print("User Disconnected")
        if sock in self.__OUTPUTS:
            self.__OUTPUTS.remove(sock)
        if sock in self.__WRITABLE:
            self.__WRITABLE.remove(sock)
        self.__INPUTS.remove(sock)
        sock.close()
        username = self.__MESSAGE_QUEUES[sock]
        try:
            self.conClients.remove(username)
        except:
            pass

        del self.__MESSAGE_QUEUES[sock]

    def __handler(self,__receivingMsg, __varifiedDevices):
        while True:

            for i,_data_ in enumerate(__receivingMsg):
                r_data = pickle.loads(b64decode(_data_))
                if r_data[self.__SENDER_NAME] not in __varifiedDevices:
                    loaded = self.__load_object(data = _data_, secure = False)
                    try:
                        if loaded[self.__TYPE] == self.__CODE_100_NEW:
                            self.__new_client_handler(loaded)
                            __receivingMsg.pop(i)
                    except TypeError:
                        loaded = self.__load_object(data = _data_, secure = True, key_dict = self.__KEY_STORE)
                        if loaded[self.__TYPE] == self.__CODE_111_NEW:
                            self.__new_client_res(loaded)
                            __receivingMsg.pop(i)
                            
                else:
                    loaded = self.__load_object(data = _data_, secure = True, key_dict = self.__KEY_STORE)

                    if loaded is not None:        

                        if loaded[self.__TYPE] == self.__DSP_REQ:
                            if loaded[self.__TARGET_NAME] in self.VARIFIED_DEVICES:
                                self.__dsp_manager(loaded)
                                __receivingMsg.pop(i)

                        elif loaded[self.__TYPE] == self.__DSP_HR_L1:
                            if loaded[self.__TARGET_NAME] in self.VARIFIED_DEVICES:
                                self.__dsp_manager(loaded)
                                __receivingMsg.pop(i)

                        elif loaded[self.__TYPE] == self.__DSP_HR_L2:
                            if loaded[self.__TARGET_NAME] in self.VARIFIED_DEVICES:
                                self.__dsp_manager(loaded)
                                __receivingMsg.pop(i)

                        elif loaded[self.__TYPE] == self.__DSP_MSG:
                            if loaded[self.__TARGET_NAME] in self.VARIFIED_DEVICES:
                                self.__dsp_manager(loaded)
                                __receivingMsg.pop(i)

                        elif loaded[self.__TYPE] in self.__CUSTOM_CHANNEL:
                            self.__custom_msg_handler(loaded)
                            __receivingMsg.pop(i)

    def __new_client_handler(self,data):
        qw = {
            self.__AES_KEY : AESGCM.generate_key(256),
            self.__NONCE : urandom(32),
            self.__AAD : bytes(self.name_generator(),encoding_one),
        }
        key_pack = b64encode(pickle.dumps(qw))
        key = load_ssh_public_key(
            bytes(
                data[self.__DATA],
                encoding_one
            ),
            backend=default_backend()
        )
        ciphertext = key.encrypt(
            key_pack,
            OAEP(
                mgf = MGF1(algorithm = SHA256()),
                algorithm = SHA256(),
                label = None
            )
        )
        OBJECT = {
            self.__TYPE : self.__CODE_110_NEW,
            self.__SENDER_NAME : self.__SERVER,
            self.__TARGET_NAME : data[self.__USERNAME],
            self.__DATA : ciphertext
        }

        normalized = self.__serializer(object = OBJECT, secure = False)
        self.__SENDER_QUEUE.append([data[self.__USERNAME], normalized])
        self.code001_AN(
            file = self.__file_location,
            key = self.__KEY,
            target_key = data[self.__USERNAME],
            value = [self.__UNVARIFIED,key_pack]
        )
        self.__KEY_STORE[data[self.__USERNAME]] = [self.__UNVARIFIED,key_pack]

    def __new_client_res(self,data):
        if data[self.__DATA] == self.__SAVE:
            target_name = data[self.__SENDER_NAME]
            self.code001_UN(
                file = self.__file_location,
                key = self.__KEY,
                target_key = target_name,
                position = 0,
                value = self.__VARIFIED
            )
            self.__KEY_STORE[target_name] = [ self.__VARIFIED, self.__KEY_STORE[target_name][1] ]
            self.VARIFIED_DEVICES.append(data[self.__SENDER_NAME])

    def __dsp_manager(self,data):
        normalized = self.__serializer(
            object = data,
            secure = True,
            key_dict = self.__KEY_STORE
        )
        self.__SENDER_QUEUE.append(
            [
                data[self.__TARGET_NAME],
                normalized
            ]
        )

    def __custom_msg_handler(self,data):
        self.__MESSAGE_HANDLER.append(data)

    def __sender(self, __writable, __senderQueue):
        while True:

            for s in __writable:
                if s._closed and s.fileno() == -1:
                    __writable.remove(s)

                try:
                    username = self.__MESSAGE_QUEUES[s]
                except KeyError:
                    pass

                sender_q = list(zip(*__senderQueue))

                if len(sender_q) > 0:
                    if username in sender_q[0]:
                        INDEX = sender_q[0].index(username)
                        prepare_send = sender_q[1][INDEX]
                        s.send(str(len(prepare_send)).center(16,"|").encode(encoding_one))
                        s.send(prepare_send)
                        __senderQueue.pop(INDEX)

    def __callback(self,__callback_lst):
        while True:
            for i,func in enumerate(__callback_lst):
                __callback_lst.pop(i)
                func[0](*func[1])

    def CREATE_CHANNEL(self, channels : str = None, multiple : bool = False):
        if not multiple:
            if type[channels] == type([]):
                raise ValueError("'channels' should be a string when multiple is set to False.")

        if multiple:
            if type(channels) is type([]):
                for channel in channels:
                    if channel not in self.__CUSTOM_CHANNEL:
                        self.__CUSTOM_CHANNEL.append(channel)
        else:
            if channels not in self.__CUSTOM_CHANNEL:
                self.__CUSTOM_CHANNEL.append(channels)

    def SEND(self, target_name, channel : str = None, data = None):

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

                prepare_send_data = {
                    self.__TYPE : channel,
                    self.__SENDER_NAME : self.__SERVER,
                    self.__TARGET_NAME : target_name,
                    self.__DATA : data
                }

                normalized = self.__serializer(
                    object = prepare_send_data,
                    secure = True,
                    key_dict = self.__KEY_STORE
                )

                self.__SENDER_QUEUE.append([target_name, normalized])
        else:
            raise TypeError(f"unallowed / untransmitable type of argument 'data', {type(data)}")


    def LISTEN(self,channel : str = None, function : object = None, args = None):
        
        if not channel:
            raise TypeError("LISTEN() missing 1 required positional argument: 'channel'")
        else:
            found = False
            index = None

            if channel in self.__CUSTOM_CHANNEL:
                for i,d in enumerate(self.__MESSAGE_HANDLER):
                    if d[self.__TYPE] == channel:
                        found = True
                        index = i
                        break
                
                if found:
                    if not args:
                        p_data = self.__MESSAGE_HANDLER.pop(index)
                        
                        p_data["sender_name"] = pickle.loads(b64decode(p_data["sender_name"]))
                        p_data["target_name"] = pickle.loads(b64decode(p_data["target_name"]))
                        self.__CALLBACK_LOOP.append([function,[p_data]])
                    else:
                        p_data = self.__MESSAGE_HANDLER.pop(index)
                        p_data["sender_name"] = pickle.loads(b64decode(p_data["sender_name"]))
                        p_data["target_name"] = pickle.loads(b64decode(p_data["target_name"]))
                        args = list(args)
                        args.insert(0,p_data)
                        self.__CALLBACK_LOOP.append([function,args])


class Sserver():
    def __init__(self, file = None, debug : bool = False, MTCL : bool = True, MPCL : bool = False, safeMode : bool = True):
        """
        This class allows user to create multi-client server.
        args: 
            secure : bool = True -> this should set to the default value True,
            file : str = None -> here user need to pass a yaml file which saves all the keys and configurations.
                if not specified, will raise an TypeError
        """

        if not file:
            raise TypeError("asyncServer() missing 1 required positional argument: 'file'")

        __parent = MAIN(file,debug,MTCL,MPCL,safeMode)

        self.SERVER = __parent.SERVER
        self.CREATE_CHANNEL  = __parent.CREATE_CHANNEL
        self.LISTEN = __parent.LISTEN
        self.SEND = __parent.SEND
        self.conClients = __parent.conClients
        self.varifiedDevices = __parent.VARIFIED_DEVICES

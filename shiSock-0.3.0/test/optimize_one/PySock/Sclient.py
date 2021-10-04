import socket
import pickle
import hashlib #
from random import sample, shuffle

urandom = pickle.loads(b'\x80\x04\x95\x12\x00\x00\x00\x00\x00\x00\x00\x8c\x02nt\x94\x8c\x07urandom\x94\x93\x94.')
mThread = pickle.loads(b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00\x8c\tthreading\x94\x8c\x06Thread\x94\x93\x94.') # done
rsa_private_key = pickle.loads(b'\x80\x04\x95J\x00\x00\x00\x00\x00\x00\x00\x8c-cryptography.hazmat.primitives.asymmetric.rsa\x94\x8c\x14generate_private_key\x94\x93\x94.')
Encoding = pickle.loads(b'\x80\x04\x95>\x00\x00\x00\x00\x00\x00\x00\x8c-cryptography.hazmat.primitives._serialization\x94\x8c\x08Encoding\x94\x93\x94.')
PublicFormat = pickle.loads(b'\x80\x04\x95B\x00\x00\x00\x00\x00\x00\x00\x8c-cryptography.hazmat.primitives._serialization\x94\x8c\x0cPublicFormat\x94\x93\x94.')
PrivateFormat = pickle.loads(b'\x80\x04\x95C\x00\x00\x00\x00\x00\x00\x00\x8c-cryptography.hazmat.primitives._serialization\x94\x8c\rPrivateFormat\x94\x93\x94.')
BestAvailableEncryption = pickle.loads(b'\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00\x8c-cryptography.hazmat.primitives._serialization\x94\x8c\x17BestAvailableEncryption\x94\x93\x94.')
load_pem_private_key = pickle.loads(b'\x80\x04\x95N\x00\x00\x00\x00\x00\x00\x00\x8c1cryptography.hazmat.primitives.serialization.base\x94\x8c\x14load_pem_private_key\x94\x93\x94.')
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
now = pickle.loads(b'\x80\x04\x95:\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94\x8c\x03now\x94\x86\x94R\x94.')
timedelta = pickle.loads(b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00\x8c\x08datetime\x94\x8c\ttimedelta\x94\x93\x94.')

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
        # print(key)
        if key == None:
            return self.read_yml(file)
        
        if wait:
            while True:
                r_yml = self.read_yml(file)
                try:
                    value = r_yml[key]
                    return value
                except KeyError:
                    # print("key not found")
                    pass

                except TypeError:
                    pass
        else:
            r_yml = self.read_yml(file)
            try:
                value = r_yml[key]
                return value
            except KeyError:
                # print("key not found")
                return None

            except TypeError:
                pass

    def remove_node(self,file,node):
        try:
            r_yml = self.read_yml(file = file)
            r_yml[node]
            r_yml.pop(node)
            self.write_yml(file = file, dict_data = r_yml, mode = "w")
            
        except KeyError:
            print("key not found")
            #pass
        except:
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

    def code001_AN(self,file = None, key = None ,target_key = None, value = None, first_time = False):
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

class Main(IPNC):

    def __init__(self,client_name : str = None, file : str = None, debug : bool = False, rememberServer = True, MPCL : bool = False, MTCL : bool = True):

        self.__KEY = b',p\xe1+z\x06F\xf9"y\xf4\'\xc7\xb3\x8es4\xd8\xe58\x9c\xff\x16z\x1d\xc3\x0es\xf8&\xb6\x83'
        self.__SECURE = b'j\x93KE\x14N7X\x91\x1e\xfa)\xedh\xfb-B\x0f\xa7\xbdV\x879\xcd\xcd\xa9%\x1f\xa9`\x9b\x1e'
        self.__SENDER_NAME = b'\xda\x0fb\xe5ihB\x1aeJ7\xe3\x82\xca.!~|pS;\xdavy\x89\x93d\xcb\x02\xb4\xe9U'
        self.__AES_KEY = b':w\\\tm\xbb\x7f\xee\xf40\x93\xbf\x9b\xc8@=\xb6\x05\x84q\xacm)\x88+\xf7\xcd\x0e\xf4\xdb\xf5\x92'
        self.__NONCE = b'x7{RWW\xb4\x94B\x7f\x89\x01O\x97\xd7\x99(\xf3\x93\x8d\x14\xebQ\xe2\x0f\xb5\xde\xc9\x83N\xb3\x04'
        self.__DATA = b':n\xb0y\x0f9\xac\x87\xc9O8V\xb2\xdd,]\x11\x0eh\x11`"a\xa9\xa9#\xd3\xbb#\xad\xc8\xb7'
        self.__AAD = b'~\x9eZ\xc3\x0f"\x16\xfd\x0f\xd6\xf5\xfa\xed1o-Y\x836\x1aB\x03\xc33\x0c\xfaF\xefe\xbbGg'
        self.__TARGET_NAME = b'\x031\xec\xa7P\xcb|\xb6\xb9(\xbdY\xb8m\x07\xd4\x826\x90C\xc5\xcc\xa0\xe1\xaa\x82YH\xbc\xcb\xf4\xa5'
        self.__SERVER = b'\xb3\xea\xcd3C;1\xb5%#Q\x03,\x9b>z.z\xa7s\x8d]\xec\xdf\r\xd6\xc6&\x80\x85<\x06'
        self.__TYPE = b'\x13\x03\xc0k\x0b\x01M\x0c\xe7\xb9\x88\xab\x17:\x13\xf3\x12\'\xd4\x17\x05\x8f\xf4\xbb\xe6\xf8\xc2"\xb4\xad\x91<'
        self.__CODE_100_NEW = b'w\xc0\x88]\xb8\xafE\xd1\xcc\x8c\x84\x80\x16\x1f\xa5\x9a\x90\x8d\xa1\x9c\x92\xedej\xec\x08\x96g\xea\xc8\x8d\xd7'
        self.__CODE_110_NEW = b'=\x9b\x82I\x12b\x8d\xdf>\xfa\xa47O\x82\xea\x95j]\xc7^\xaa\x89\xa4\x95\xb8\xa3\xd0\x1fi\xeb\xbf\xa5'
        self.__CODE_111_NEW = b'\x17\xca\xa1V\xa1\xa4\xb4\xd7\x87y\xf9k6_\x8e\x1e\xfd\xa2m\xb5\x1b\xc1\xaf+\xbf\xc2\xf7\x96-\xa9&y'
        self.__DSP_REQ = b'a\xc2\xd4\x16\x0fheI\xcc\x07O\xddhC8\x0f.\x03\xe9\xa5\xad\xfe\xc0\x91&\xb7\xbd\x8c\x12\xf8\xf3M'
        self.__DSP_HR_L1 = b'4D\xc7\xf6\x18\xba\xae\xbf1\x04F\x07M\x05\x02\x0f\xe39y\xc9~\x0eD\xa1\x9c%\xbf5q^\xa7b'
        self.__DSP_HR_L2 = b'\xef\x1a\xd0M\xf9\x99S\x1cj\xab\xa0\xa7\x1a\x91\xa5\xbeQ\x94\x11\xb9wEp\x08\xcf>\x0e\xa1\xb8\xe9q\xec'
        self.__DSP_MSG = b'\xa2V\xf6y\x1a\xe2-\xf1\x9c\xf0h\xf2\x7f\x82\xef4\xa8\xbe\x19\x15rm\x02U\x0e\xcd3;{\xa7u\x1d'
        self.__USERNAME = b'\x16\xf7\x8a}c\x17\xf1\x02\xbb\xd9_\xc9\xa4\xf3\xff.2I(v\x90\xb8\xbd\xadkx\x10\xf8+4\xac\xe3'
        self.__VARIFIED = b'\x1d\xc2D\x88\xda\x8d\x18b*\xa0\xc5\x02\x8c=\xb4\xfb\xed\xe6@\x88\xd9lU\x13\xbd\xd0\x06j\xfa\x81\x83\x90'
        self.__UNVARIFIED = b'\xf9\x1c\r|\xd6\xdb\xab\x1c\xcc\x10\xf8\xed\x0e\xe1i\xc33\xf0\x86\xd54\xb86\x8ee\x96\xb9Z\x8bU\xc8X'
        self.__SAVE = b'\x15}\xca\x92\xe4%\x04X3\x9dK\x83RP\xd4L#\x8f3U\xe1\xb7\x98a\x95\x18\x8e\xe44\xe9\xba\xff'
        self.__STATUS = b"\x07<\x164\xc4\x96\xcd\xb6I\xd1\xaf\xe0\xa3\x12\xbb\xb4\xb7\xe1t\x1b'\x15B\xe4\xa46\xc3\xb8\x82K\x17a"
        self.__APPROVED = b'&\x87\xf8n\xd6xK\x8a_\xca6\xe6\xc4h\xe1*\xa4M\xc3\xc7\xe8\x13~1`\xd1\xa9Py\xbd\xcd\x02'
        self.__BYPASSPIPE = b'\x1d\xcc\xea0\x9d)Szj\x02\xab\x8b\xf4\x01\x94\x914\x1d\x89X\xd18\xf2\xe3\xa8\xd49\xac\xb2\x00\xb6S'
        self.__CODE_001_SRT_KEY = b'\x92\x94{\xbdb5\xe1>"\xe3\xf8t\x8c*\x0c\xf4\xdfu\x99Q\x1cKc\xcf\xe9\xcf\r\x03\x8c\xf1\xc7\x18'

        self.encoding_one = "utf-8"
        
        IPNC.__init__(self)

        self.__debug = debug

        if not file:
            raise TypeError("__init__() missing 1 required positional argument: 'file'")
        else:
            self.__file_location = file
            # self.__client_name = hashlib.sha256(bytes(client_name,self.encoding_one)).digest()
            self.__client_name = client_name

        if MPCL and MTCL:
            raise ValueError("both 'MPCL' abd 'MTCL' should not be set to True")

        elif not MPCL and not MTCL:
            raise ValueError("both 'MPCL' abd 'MTCL' should not be set to False")

        else:
            self.__MPCL = MPCL
            self.__MTCL = MTCL

        self.__CUSTOM_CHANNEL = []
        self.__MESSAGE_HANDLER = []
        self.__CALLBACK_LOOP = []
        self.__SENDER_QUEUE = []
        self.HS_Devices = []
        self.__KEY_STORE ={}

        if rememberServer:

            __get = self.get_node(file = self.__file_location,key = self.__VARIFIED, wait = False)
          
            if __get == None:
                self.add_node(
                    file=self.__file_location,
                    node=[
                        self.__VARIFIED,
                        pickle.dumps(False)
                    ]
                )

            __code003_hs_key = self.get_node(
                file = self.__file_location,
                key = self.__KEY,
                wait = False
            )

            if __code003_hs_key is not None:
                # print(f"__code003_hs_key : {__code003_hs_key}")

                self.__KEY_STORE = __code003_hs_key

                self.HS_Devices = [k for (k,v) in __code003_hs_key.items() if v[0] == self.__VARIFIED]


            __code001_key = self.get_node(
                file = self.__file_location,
                key = self.__CODE_001_SRT_KEY,
                wait = False
            )

            if __code001_key is not None:
                if __code001_key[self.__STATUS] == self.__VARIFIED:
                    self.__KEY_STORE[self.__CODE_001_SRT_KEY] = __code001_key[self.__KEY]

        self.__CUSTOM_CHANNEL.append(self.__DSP_MSG)
        self.__VARIFIED = self.get_node(
            file = self.__file_location,
            key = self.__VARIFIED,
            wait = False
        )
        self.__VARIFIED = pickle.loads(self.__VARIFIED)

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

            key_pack = pickle.loads(b64decode(key_dict[self.__CODE_001_SRT_KEY]))

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

        # target = object[self.__TARGET_NAME]
        normalize = b64encode(pickle.dumps(object))

        if secure:

            key_pack = pickle.loads(b64decode(key_dict[self.__CODE_001_SRT_KEY]))

            aes_gcm = AESGCM(key_pack[self.__AES_KEY])
            cyphertext = aes_gcm.encrypt(
                nonce = key_pack[self.__NONCE],
                data = normalize,
                associated_data = key_pack[self.__AAD]
            )

            prepare_serialized_data = {self.__SECURE : secure, self.__SENDER_NAME : self.__client_name, self.__DATA : cyphertext}
            flatten_psd = b64encode(pickle.dumps(prepare_serialized_data))

            return flatten_psd
        else:

            prepare_serialized_data = {self.__SECURE : secure, self.__SENDER_NAME : self.__client_name, self.__DATA : normalize}
            flatten_psd = b64encode(pickle.dumps(prepare_serialized_data))

            return flatten_psd
    
    def CLIENT(self,address : str = None, port : int = None,timeout : int = 1):
        
        if self.__debug:
            print("[Connecting TO Server]")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address, port))

        if self.__debug:
            print("[Connected]")

        
        receiver_thread = mThread(target=self.__receiver)

        sender_thread = mThread(
            target = self.__sender,
            args = (self.sock, self.__SENDER_QUEUE)
        )

        if self.__MTCL:
            callback_loop_thread_process = mThread(
                target = self.__callback_lopp,
                args = (self.__CALLBACK_LOOP,)
            )
        elif self.__MPCL:
            callback_loop_thread_process = mProcess(
                target = self.__callback_loop,
                args = (self.__CALLBACK_LOOP,)
            )

        receiver_thread.daemon = True
        sender_thread.daemon = True
        callback_loop_thread_process.daemon = True

        receiver_thread.start()
        sender_thread.start()
        callback_loop_thread_process.start()

        if not self.__VARIFIED:

            code_001_srt_key = rsa_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )

            code_001_key = code_001_srt_key.public_key()
            str_code_001_key = code_001_key.public_bytes(
                Encoding.OpenSSH,
                PublicFormat.OpenSSH
            ).decode()

            OBJECT = self.__serializer(
                    object = {self.__TYPE : self.__CODE_100_NEW, self.__USERNAME : self.__client_name, self.__DATA : str_code_001_key},
                    secure = False
                )

            self.sock.send(str(len(OBJECT)).center(16,"|").encode(self.encoding_one))
            self.sock.send(OBJECT)

            # self.code001_AN(
            #     file = self.__file_location,
            #     key = self.__CODE_001_SRT_KEY,
            #     target_key = 
            # )

            self.add_node(
                file = self.__file_location,
                node = [
                    # hashlib.sha256(bytes(self.__CODE_001_SRT_KEY,self.encoding_one)).digest(),
                    self.__CODE_001_SRT_KEY,
                    {
                        self.__STATUS : self.__UNVARIFIED,
                        self.__KEY : code_001_srt_key.private_bytes(
                        encoding=Encoding.PEM,
                        format=PrivateFormat.PKCS8,
                        encryption_algorithm=BestAvailableEncryption(
                            b'aw56hfseyinhy7fce4ser')
                    )
                    }
                ]
            )

            count_time = now() + timedelta(minutes = timeout)
            while now() <= count_time and not self.__VARIFIED:
                pass
                
            if not self.__VARIFIED:
                raise TimeoutError("could not varified by server, try again!")
        else:

            OBJECT = self.__serializer(
                    object = {self.__TYPE : "_", self.__USERNAME : self.__client_name, self.__DATA : ""},
                    secure = False
                )

            self.sock.send(str(len(OBJECT)).center(16,"|").encode(self.encoding_one))
            self.sock.send(OBJECT)    

    def __receiver(self):
        while True:
            if not self.__VARIFIED:
                data_len = int(self.sock.recv(16).decode().strip("|"))
                if not data_len:
                    self.sock.close()
                    # pair -a1.1
                    #need future attention----------------------------------------------------------------------

                else:
                    recv_data = self.sock.recv(data_len)

                    _info = self.__load_object(
                        data = recv_data,
                        secure = False
                    )
                    # print(f"_info_ : {_info}")

                    # _info = {self.__TYPE = "code-0.0.1-key-res", self.__SENDER_NAME : self.__SERVER, self.__DATA : "encrypted aes key pack"}

                    if _info[self.__TYPE] == self.__CODE_110_NEW and _info[self.__SENDER_NAME] == self.__SERVER:

                        code001_key_load = self.get_node(
                            file = self.__file_location,
                            # key = hashlib.sha256(bytes(self.__CODE_001_SRT_KEY,self.encoding_one)).digest()
                            key = self.__CODE_001_SRT_KEY
                        )

                        # print(code001_key_load)

                        if code001_key_load[self.__STATUS] == self.__UNVARIFIED :

                            code_001_srt_key = load_pem_private_key(
                                data = code001_key_load[self.__KEY],
                                password=b'aw56hfseyinhy7fce4ser',
                                backend=default_backend()
                            )

                            key_pack = code_001_srt_key.decrypt(
                                ciphertext = _info[self.__DATA ],
                                padding = OAEP(
                                    mgf = MGF1(
                                        algorithm = SHA256()
                                    ),
                                    algorithm = SHA256(),
                                    label = None
                                )
                            )

                            self.add_node(
                                file = self.__file_location,
                                node = [
                                    # hashlib.sha256(bytes(self.__CODE_001_SRT_KEY,self.encoding_one)).digest(),
                                    self.__CODE_001_SRT_KEY,
                                    {
                                        self.__STATUS : self.__VARIFIED ,
                                        self.__KEY : key_pack
                                    }
                                ]
                            )

                            self.__KEY_STORE[self.__CODE_001_SRT_KEY] = key_pack

                            OBJECT = {
                                self.__TYPE : self.__CODE_111_NEW,
                                self.__SENDER_NAME : self.__client_name,
                                self.__TARGET_NAME : self.__SERVER,
                                self.__DATA : self.__SAVE
                            }

                            normalized = self.__serializer(
                                object = OBJECT,
                                secure = True,
                                key_dict = self.__KEY_STORE
                            )

                            self.__SENDER_QUEUE.append(normalized)

                            self.__VARIFIED = True

                            self.add_node(
                                file = self.__file_location,
                                node=[
                                    self.__VARIFIED,
                                    pickle.dumps(True)
                                ]
                            )

            else:
                data_len = int(self.sock.recv(16).decode().strip("|"))
                if not data_len:
                    self.sock.close()
                    # pair -a1.2
                else:
                    recv_data = self.sock.recv(data_len)
                    code_002 = self.__load_object(
                        data = recv_data,
                        secure = True,
                        key_dict = self.__KEY_STORE
                    )

                    # code_002 = {self.__TYPE = "xyz", self.__BYPASSPIPE : self.__SERVER, self.__SENDER_NAME : "xyz", self.__TARGET_NAME : "abc", self.__DATA : "pqr"}
                    # handshake counter part
                    if code_002[self.__TYPE] == self.__DSP_REQ:

                        if code_002[self.__TARGET_NAME] == self.__client_name:

                            M_code002_k_pack = {
                                self.__AES_KEY : AESGCM.generate_key(256),
                                self.__NONCE  : urandom(32),
                                self.__AAD : bytes(self.name_generator(),self.encoding_one),
                                self.__APPROVED : True
                            }
                            normalized_M_code002_k_pack = b64encode(pickle.dumps(M_code002_k_pack))

                            rsa_key =load_ssh_public_key(
                                bytes(code_002[self.__DATA],self.encoding_one),
                                backend=default_backend()
                            )


                            ciphertext = rsa_key.encrypt(
                                normalized_M_code002_k_pack,
                                OAEP(
                                    mgf = MGF1(algorithm = SHA256()),
                                    algorithm = SHA256(),
                                    label = None
                                )
                            )

                            OBJECT = {
                                self.__TYPE : self.__DSP_HR_L1,
                                self.__BYPASSPIPE : self.__SERVER,
                                self.__SENDER_NAME : self.__client_name,
                                self.__TARGET_NAME : code_002[self.__SENDER_NAME],
                                self.__DATA : ciphertext
                            }

                            normalized = self.__serializer(
                                object = OBJECT,
                                secure = True,
                                key_dict = self.__KEY_STORE
                            )

                            self.__SENDER_QUEUE.append(normalized)

                            del M_code002_k_pack[self.__APPROVED]

                            code001_AN_value = b64encode(pickle.dumps(M_code002_k_pack))

                            self.code001_AN(
                                file = self.__file_location,
                                key = self.__KEY,
                                target_key  = code_002[self.__SENDER_NAME],
                                value = [self.__UNVARIFIED,code001_AN_value]
                            )

                            self.__KEY_STORE[code_002[self.__SENDER_NAME]] = [self.__UNVARIFIED,code001_AN_value]
                            
                            if self.__debug:
                                print(f"HS from : {code_002[self.__SENDER_NAME]} | step_1 Done")

                    # code_002 = {self.__TYPE = "xyz", self.__BYPASSPIPE : self.__SERVER, self.__SENDER_NAME : "xyz", self.__TARGET_NAME : "abc", self.__DATA : "pqr"}
                    # type DSP-HR counter part
                    elif code_002[self.__TYPE] == self.__DSP_HR_L1:

                        if code_002[self.__TARGET_NAME] == self.__client_name:

                            flatten_key = pickle.loads(b64decode(self.__KEY_STORE[code_002[self.__SENDER_NAME]]))[1]
                            
                            loaded_code_003_srt = load_pem_private_key(
                                data = flatten_key,
                                password = b'oieffjwouifh2398r29r8238h38h923h8983',
                                backend = default_backend()
                            )

                            __code_003_aes_srt = loaded_code_003_srt.decrypt(
                                ciphertext = code_002[self.__DATA],
                                padding = OAEP(
                                    mgf = MGF1(
                                        algorithm = SHA256()
                                    ),
                                    algorithm = SHA256(),
                                    label = None
                                )
                            )

                            __code_003_aes_srt = pickle.loads(b64decode(__code_003_aes_srt))
                            
                            if __code_003_aes_srt[self.__APPROVED]:

                                OBJECT = {
                                    self.__TYPE : self.__DSP_HR_L2,
                                    self.__BYPASSPIPE : self.__SERVER,
                                    self.__SENDER_NAME : self.__client_name,
                                    self.__TARGET_NAME : code_002[self.__SENDER_NAME],
                                    self.__DATA : hashlib.sha256(bytes(self.__APPROVED,self.encoding_one)).digest()

                                }

                                del __code_003_aes_srt[self.__APPROVED]

                                __code_003_aes_srt = b64encode(pickle.dumps(__code_003_aes_srt))
                                                                
                                normalized = self.__serializer(
                                    object = OBJECT,
                                    secure = True, 
                                    key_dict = self.__KEY_STORE
                                )

                                self.__SENDER_QUEUE.append(normalized)

                                self.code001_UN(
                                    file = self.__file_location,
                                    key = self.__KEY,
                                    target_key = code_002[self.__SENDER_NAME],
                                    position = None,
                                    value = [self.__VARIFIED,__code_003_aes_srt]
                                )

                                self.__KEY_STORE[code_002[self.__SENDER_NAME]] = b64encode(pickle.dumps([self.__VARIFIED,__code_003_aes_srt]))
                                self.HS_Devices.append(code_002[self.__SENDER_NAME])

                                print("Done")

                    # "DSP-HRR-L1" counter part
                    elif code_002[self.__TYPE] == self.__DSP_HR_L1 :
                        if code_002[self.__TARGET_NAME] == self.__client_name:
                            if code_002[self.__DATA] == hashlib.sha256(bytes(self.__APPROVED,self.encoding_one)).digest():

                                self.code001_UN(
                                    file = self.__file_location,
                                    key = self.__KEY,
                                    target_key = code_002[self.__SENDER_NAME],
                                    position = 0,
                                    value = self.__VARIFIED
                                )

                                self.__KEY_STORE[code_002[self.__SENDER_NAME]] = b64encode(pickle.dumps(
                                            [
                                                self.__VARIFIED,
                                                self.__KEY_STORE[code_002[self.__SENDER_NAME]][1]
                                            ]
                                        )
                                    )
                                

                                self.HS_Devices.append(code_002[self.__SENDER_NAME])

                                print(f"Handshake from {code_002[self.__SENDER_NAME ]} Done")

                    elif code_002[self.__TYPE] == self.__DSP_MSG :
                        code_004_key = self.__KEY_STORE[code_002[self.__SENDER_NAME]]
                        code_004_key = pickle.loads(b64decode(code_004_key[1]))
                        aes_gcm = AESGCM(code_004_key[self.__AES_KEY])
                        decryptedtext = aes_gcm.decrypt(
                            nonce = code_004_key[self.__NONCE], 
                            data = code_002[self.__DATA],
                            associated_data = code_004_key[self.__AAD]
                        )
                        data = pickle.loads(b64decode(decryptedtext))
                        code_002[self.__DATA] = data
                        self.__MESSAGE_HANDLER.append(code_002)

                    elif code_002[self.__TYPE] in self.__CUSTOM_CHANNEL:
                        self.__MESSAGE_HANDLER.append(code_002)

                    
            

    def __sender(self, sock, __sender_queue):
        while True:
            for i,data in enumerate(__sender_queue):
                sock.send(str(len(data)).center(16,"|").encode(self.encoding_one))
                sock.send(data)
                __sender_queue.pop(i)

    def __callback_lopp(self,__callback_lst):
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

    def HANDSHAKE(self,target_name : str = None):

        if self.__debug:
            print("Doing Handshake...")
            
        # target_name = hashlib.sha256(target_name).digest()

        try:
            check = self.__KEY_STORE[target_name]
        except KeyError:
            check = None

        if check is not None:

            if len(check) > 0 or check is None:
                if self.__debug:
                    print(f"{target_name} : already handshaked OR have the request for handshake.")

        else:
            __code_002_srt_key = rsa_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            __code_002_pub_key = __code_002_srt_key.public_key()
            str_code_002_pub_key = __code_002_pub_key.public_bytes(
                Encoding.OpenSSH,
                PublicFormat.OpenSSH
            ).decode()

            # print(f"str_code_002_pub_key : {str_code_002_pub_key}") #===============

            OBJECT = {
                self.__TYPE : self.__DSP_REQ,
                self.__BYPASSPIPE : self.__SERVER,
                self.__SENDER_NAME : self.__client_name,
                self.__TARGET_NAME : target_name,
                self.__DATA : str_code_002_pub_key
                }

            normalised = self.__serializer(
                object = OBJECT,
                secure = True,
                key_dict = self.__KEY_STORE
            )

            self.__SENDER_QUEUE.append(normalised)

            __code_003_srt_key_str = __code_002_srt_key.private_bytes(
                encoding=Encoding.PEM,
                format=PrivateFormat.PKCS8,
                encryption_algorithm=BestAvailableEncryption(
                    b'oieffjwouifh2398r29r8238h38h923h8983')
            )

            self.code001_AN(
                file = self.__file_location,
                key = self.__KEY,
                target_key = target_name,
                value = [
                    self.__UNVARIFIED,
                    __code_003_srt_key_str
                ]
            )
            self.__KEY_STORE[target_name] = b64encode(pickle.dumps([self.__UNVARIFIED,__code_003_srt_key_str]))

            if self.__debug:
                print("Handshake Request Send.")

        

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
                        self.__CALLBACK_LOOP.append([function,[p_data]])
                    else:
                        p_data = self.__MESSAGE_HANDLER.pop(index)
                        args = list(args)
                        args.insert(0,p_data)
                        self.__CALLBACK_LOOP.append([function,args])

    def SEND(self,channel : str = None, data = None):

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
                    self.__BYPASSPIPE : self.__SERVER,
                    self.__SENDER_NAME : self.__client_name,
                    self.__TARGET_NAME : self.__SERVER,
                    self.__DATA : data
                }

                normalized = self.__serializer(
                    object = prepare_send_data,
                    secure = True,
                    key_dict = self.__KEY_STORE
                )

                self.__SENDER_QUEUE.append(normalized)
        else:
            raise TypeError(f"unallowed / untransmitable type of argument 'data', {type(data)}")

    def SEND_TO_CLIENT(self, target_name : str = None, data = None):

        if not target_name:
            raise TypeError("SEND() missing 1 required positional argument: 'target_name'")
        if not data:
            raise TypeError("SEND() missing 1 required positional argument: 'data'")

        lst = [ [1,2], {"a":1}, (1,2), {1,2,}, "a", 12, 0.45, b"bytes" ]
        allowed_lst= []
        for l in lst:
            allowed_lst.append(type(l))
        
        if type(data) in allowed_lst:

                try:
                    code_004_key = self.__KEY_STORE[target_name]
                except KeyError:
                    raise DspError(f"{target_name} is not registered/ handshaked client")

                if code_004_key[0] == self.__VARIFIED:
                    __code_004_srt_key = pickle.loads(b64decode(code_004_key[1]))

                    aes_gcm = AESGCM(__code_004_srt_key[self.__AES_KEY])
                    ciphertext = aes_gcm.encrypt(
                        nonce = __code_004_srt_key[self.__NONCE],
                        data = b64encode(pickle.dumps(data)),
                        associated_data = __code_004_srt_key[self.__AAD]
                    )

                    OBJECT = {
                        self.__TYPE : self.__DSP_MSG ,
                        self.__BYPASSPIPE : self.__SERVER,
                        self.__TARGET_NAME : target_name,
                        self.__SENDER_NAME : self.__client_name,
                        self.__DATA : ciphertext
                    }

                    normalized = self.__serializer(
                        object = OBJECT,
                        secure = True,
                        key_dict = self.__KEY_STORE
                    )

                    self.__SENDER_QUEUE.append(normalized)
        else:
            raise TypeError(f"unallowed / untransmitable type of argument 'data', {type(data)}")

class Sclient():

    def __init__(self,client_name : str = None, file : str = None, debug : bool = False, rememberServer = True, MPCL : bool = False, MTCL : bool = True):
        
        __parent  = Main(client_name,file,debug, rememberServer, MPCL,MTCL)

        self.CLIENT = __parent.CLIENT
        self.HS_Devices = __parent.HS_Devices
        self.CREATE_CHANNEL = __parent.CREATE_CHANNEL
        self.LISTEN = __parent.LISTEN
        self.HANDSHAKE = __parent.HANDSHAKE
        self.SEND = __parent.SEND
        self.SEND_TO_CLIENT = __parent.SEND_TO_CLIENT


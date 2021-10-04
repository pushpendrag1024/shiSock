import timeit
import Sserver

Sserver.Sserver('test.yaml')

py = timeit.timeit("Sserver.Sserver('test.yaml')",setup = ('import Sserver'), number = 1000)
op = timeit.timeit("Sserver_optimized.Sserver('test.yaml')",setup = ('import Sserver_optimized'), number = 1000)

print(f"Server Takes => {py} | Server_optimized Takes => {op}")
# import time

# s1 = time.time()

# import pickle
# import socket
# from random import sample, shuffle
# import os
# import select
# import base64
# import threading
# import multiprocessing
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.ciphers.aead import AESGCM
# from cryptography.hazmat.primitives.serialization import load_ssh_public_key
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.backends import default_backend
# import yaml

# t1 = time.time() - s1

# s2 = time.time()

# urandom = pickle.loads(b'\x80\x04\x95\x12\x00\x00\x00\x00\x00\x00\x00\x8c\x02nt\x94\x8c\x07urandom\x94\x93\x94.')
# # socket = pickle.loads(b'\x80\x04\x95\x1d\x00\x00\x00\x00\x00\x00\x00C\x19\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00\x8c\x06socket\x94h\x00\x93\x94.\x94.')
# # pickle_dumps = pickle.loads(b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c\x07_pickle\x94\x8c\x05dumps\x94\x93\x94.')
# mThread = pickle.loads(b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00\x8c\tthreading\x94\x8c\x06Thread\x94\x93\x94.') # done
# sha256 = pickle.loads(b'\x80\x04\x95\x1f\x00\x00\x00\x00\x00\x00\x00\x8c\x08_hashlib\x94\x8c\x0eopenssl_sha256\x94\x93\x94.') # done
# yaml_dump = pickle.loads(b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00\x8c\x04yaml\x94\x8c\x04dump\x94\x93\x94.') # done
# yaml_full_load = pickle.loads(b'\x80\x04\x95\x16\x00\x00\x00\x00\x00\x00\x00\x8c\x04yaml\x94\x8c\tfull_load\x94\x93\x94.') # done
# # datetime = pickle.loads(b'\x80\x04\x95\x19\x00\x00\x00\x00\x00\x00\x00\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94.')
# default_backend = pickle.loads(b'\x80\x04\x954\x00\x00\x00\x00\x00\x00\x00\x8c\x1ccryptography.hazmat.backends\x94\x8c\x0fdefault_backend\x94\x93\x94.')
# AESGCM = pickle.loads(b'\x80\x04\x95:\x00\x00\x00\x00\x00\x00\x00\x8c+cryptography.hazmat.primitives.ciphers.aead\x94\x8c\x06AESGCM\x94\x93\x94.')
# # RSA_generate_private_key = pickle.loads(b'\x80\x04\x95J\x00\x00\x00\x00\x00\x00\x00\x8c-cryptography.hazmat.primitives.asymmetric.rsa\x94\x8c\x14generate_private_key\x94\x93\x94.')
# load_ssh_public_key = pickle.loads(b'\x80\x04\x95L\x00\x00\x00\x00\x00\x00\x00\x8c0cryptography.hazmat.primitives.serialization.ssh\x94\x8c\x13load_ssh_public_key\x94\x93\x94.')
# SHA256 = pickle.loads(b'\x80\x04\x954\x00\x00\x00\x00\x00\x00\x00\x8c%cryptography.hazmat.primitives.hashes\x94\x8c\x06SHA256\x94\x93\x94.')
# OAEP = pickle.loads(b'\x80\x04\x95>\x00\x00\x00\x00\x00\x00\x00\x8c1cryptography.hazmat.primitives.asymmetric.padding\x94\x8c\x04OAEP\x94\x93\x94.')
# MGF1 = pickle.loads(b'\x80\x04\x95>\x00\x00\x00\x00\x00\x00\x00\x8c1cryptography.hazmat.primitives.asymmetric.padding\x94\x8c\x04MGF1\x94\x93\x94.')
# b64encode = pickle.loads(b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00\x8c\x06base64\x94\x8c\tb64encode\x94\x93\x94.')
# b64decode = pickle.loads(b'\x80\x04\x95\x18\x00\x00\x00\x00\x00\x00\x00\x8c\x06base64\x94\x8c\tb64decode\x94\x93\x94.')
# select = pickle.loads(b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c\x06select\x94\x8c\x06select\x94\x93\x94.')
# mProcess = pickle.loads(b"\x80\x04\x95'\x00\x00\x00\x00\x00\x00\x00\x8c\x17multiprocessing.context\x94\x8c\x07Process\x94\x93\x94.")

# t2 = time.time() - s2
# print(t1)
# print(t2)
# print(min(t1,t2))
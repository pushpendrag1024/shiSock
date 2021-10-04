import sys

from .server import server
# from .eserver import SetupIPC  # deprecated

from .client import client  # not done**
from .secureClient import secureClient  # not done**

p_name = sys.platform

if p_name == "linux":
    from .eserver import eserver
    from .esecureServer import esecureServer  # not done**
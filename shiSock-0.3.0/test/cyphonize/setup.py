from distutils.core import setup, Extension
from Cython.Build import cythonize

extension = [Extension('server_c', ['server_c.pyx'])]

setup(ext_modules = cythonize(extension))
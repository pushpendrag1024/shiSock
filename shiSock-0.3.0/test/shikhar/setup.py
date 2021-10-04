from distutils.core import setup, Extension
from Cython.Build import cythonize

extension = [Extension('shikhar', ['shikhar.pyx'])]

setup(ext_modules = cythonize(extension))
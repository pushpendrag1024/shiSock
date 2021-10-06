# this file helps use to convert the python code to c code
# C code is much faster in execution but hard to understand

from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "para",
        ["para.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(
    name='hello-parallel-world',
    ext_modules=cythonize(ext_modules),
)

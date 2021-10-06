from cython.parallel import parallel, prange
from libc.stdlib cimport abort, malloc, free

cdef Py_ssize_t idx, i, n = 100
cdef int * local_buf
cdef size_t size = 10
cdef int count = 0
cdef dict d = {"loop1" : [], "loop2" : []}

def main():
    while count < 1:

        with nogil, parallel():
            for i in xrange(0,11):
                with gil:
                    d["loop1"].append(i)

        with nogil, parallel():
            for i in xrange(12,20):
                with gil:
                    d["loop2"].append(i)

        count += 1

    return d




    
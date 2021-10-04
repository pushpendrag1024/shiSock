#!python
#cython: language_level=3

__all__ = ["shikharEncode","shikharDecode"]

from base64 import b64encode, b64decode
from random import shuffle, sample, randint
from fractions import Fraction

cdef dict a = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,
    "m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,
    "x":24,"y":25,"z":26,"?" : 0}

cdef dict b = {0:"?", 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

cdef list special = list("!@#$%^&*()~`")

cdef str data

cpdef shikharEncode(data):

    if data is None:
        raise TypeError("'shikharDecode' missing a positional argument 'data'")

    if type(data) != type('shikhar'):
        raise TypeError("'data' should be non other then str ")

    cdef str l
    cdef int i
    cdef int random_num
    cdef str qw
    cdef str new_str
    cdef int len_new_str
    cdef list samples
    cdef str asa
    cdef str join 
    cdef list specials = special

    shuffle(specials)

    qw = ""
    for l in data.lower():
        qw += str(a[l])+str(0)
    resolved_num = int(qw)

    multiply = resolved_num * 999
    new_str = ""
    for i,num in enumerate(str(multiply)):
        if num == "0":
            new_str += num
        else:
            new_str += b[int(num)]

    len_new_str = len(new_str)
    samples = sample(range(1,len_new_str),10)
    new_str_lst = list(new_str)
    for i,key in enumerate(samples):
        new_str_lst.insert(key,special[i])
    asa ="".join([b[int(x)] for x in str(999)])
    join = "".join(new_str_lst) + "|~|" + asa
    return b64encode(bytes(join,"utf-8"))

cpdef shikharDecode(b_data):

    if b_data is None:
        raise TypeError("'shikharDecode' missing a positional argument 'b_data'")

    if type(b_data) != type(b'shikhar'):
        raise TypeError("'b_data' should be non other then bytes ")

    cdef list res
    #cdef int random_num
    cdef list lst
    cdef str number_str
    cdef str char
    #cdef int number
    #cdef int real_num
    cdef list get


    res = b64decode(b_data).decode().split("|~|")
    random_num = int("".join([str(a[x]) for x in list(res[1])]))
    lst = [x for x in list(res[0]) if x not in special]
    number_str = ""
    for char in lst:
        if char == "0":
            number_str += "0"
        else:
            number_str += str(a[char])
    number = Fraction(int(number_str))
    random_num = Fraction(random_num)
    real_num = number/random_num
    get = str(real_num).split("0")
    return "".join([ b[int(x)] for x in get if x != ""])
from shikhar import shikharDecode, shikharEncode

# def shikhardecode(data):
#     shikharDecode(data)

# def shikharencode(data):
#     shikharEncode(data)

name = "swat"

encoded = shikharEncode(name)
print(encoded)

decoded = shikharDecode(encoded)
print(decoded)

import base64
def ascii2hex(input_string):
    input_hex=""
    for i in range (0, len(input_string)):
        input_hex_string="0x%x" % ord(input_string[i])
        input_hex += input_hex_string[2:4]
    return input_hex

def hex2ascii(input_string):
    decrypted_string=""
    for c in range(0, int(len(input_string)), 2):
        decrypted_string += chr(int(input_string[c:c + 2], 16))
    return decrypted_string
def bin2hex(_bin):
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    dec = 0
    for b in range(0, 4, 1):
        bit = int(_bin[3 - b])
        dec += (bit * (2 ** b))
        hex_char = characters[dec]
    return hex_char


def hex2bin(_hex):
    var = int(_hex, 16)
    byte_array = ""
    r_byte_array = ""
    for z in range(0, 4):
        _bit = int(var % 2)
        var = int(var / 2)
        r_byte_array += str(_bit)
    byte_array = r_byte_array[::-1]
    return byte_array


def bin_xor(_1, _2):
    out_xor = ""
    for i in range(0, len(_1)):
        out_xor += str(int(_1[i]) ^ int(_2[i]))
    return out_xor


def b16_x(_first, _second):
    length = len(_first)
    hex_xor = ''
    for i in range(0, length):
        or_1 = hex2bin(_first[i])
        or_2 = hex2bin(_second[i])
        x_or = bin_xor(or_1, or_2)
        hex_xor += bin2hex(x_or)
    return hex_xor
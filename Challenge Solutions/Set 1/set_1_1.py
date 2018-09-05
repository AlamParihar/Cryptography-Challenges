import base64


def enc(dec):
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                  '8', '9', '+', '/']
    return characters[dec]


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

def hex2bin_string(_hex):
    string_out=""
    for i in range (0,len(_hex)):
        string_out+=hex2bin(_hex[i])
    return string_out

def bin2b64(_bin):
    b64 = ""
    for j in range(0, 4):
        dec = 0
        var = _bin[0 + 6 * j:6 + 6 * j]
        for b in range(0, 6, 1):
            bit = int(var[(5 - b)])
            dec += (bit * (2 ** b))
        b64 += enc(dec)
    return b64


def hex2b64(_hex):
    length = len(_hex)
    count = 0
    base64 = ""
    arr = ""
    for i in range(0, length):
        arr += hex2bin(_hex[i])
        count += 1
        if (count == 6):
            base64 += bin2b64(arr)
            arr = ""
            count = 0
    return base64

def b642hex(_b64):
    hex_string=""
    bin_char=""
    count=0
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                  '8', '9', '+', '/']
    for i in range (0,len(_b64)):
        if (_b64[i] in characters):
            bin_char+='{:06b}'.format(characters.index(_b64[i]))
        else:
            bin_char='{:06b}'.format('')
        count+=1
        if count==4:
            for b in range (0,6):
                hex_string+=hex(int(bin_char[4*b:4*b+4],2))[2]

            bin_char=""
            count=0
    return  hex_string

import math
import binascii
import set_1_2

def ascii2bin(ascii_string):
    binary_string=""
    for char in ascii_string:
        binary_string+=bin(ord(char))[2:].zfill(8)

    return binary_string

def rotl(data, rot):
    return ((data << rot) | (data >> (32 - rot))) & 0xffffffff

def SHA1(message):
    #initialize values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    ml=len(message)*8
    #pre_process
    message_bin=ascii2bin(message)
    message_bin=message_bin+"1"
    while(len(message_bin)%512!=448):
        message_bin+="0"
    message_bin+=bin(ml)[2:].zfill(64)
    chunks=[]
    chunk_size=512
    num_chunks=math.ceil(len(message_bin)/chunk_size)

    for chunk_count in range(0, num_chunks):
        chunk=(message_bin[chunk_count*chunk_size:(chunk_count+1)*chunk_size])
        words=[]
        word_size=32
        for word in range(0,16):
            words.append(int(chunk[word*word_size:(word+1)*word_size], 2))

        for word in range(16, 80):
            new_word=((words[word-3] ^ words[word-8] ^ words[word-14] ^ words[word-16]))
            words.append(rotl(new_word, 1))

        a=h0
        b=h1
        c=h2
        d=h3
        e=h4

        for i in range(0,80):
            if(i<20):
                f=(b&c)|((~b)&d)
                k = 0x5A827999
            elif(i<40):
                f=(b^c)^d
                k = 0x6ED9EBA1
            elif(i<60):
                f=(b&c)|(b&d)|(c&d)
                k = 0x8F1BBCDC
            else:
                f = (b ^ c) ^ d
                k = 0xCA62C1D6



            temp=rotl(a, 5) + f + e + k + words[i] & 0xffffffff
            e=d
            d=c
            c=rotl(b, 30)
            b=a
            a=temp
        h0= h0 + a & 0xffffffff
        h1= h1 + b & 0xffffffff
        h2= h2 + c & 0xffffffff
        h3= h3 + d & 0xffffffff
        h4= h4 + e & 0xffffffff
    hh=hex((h0<<128) | (h1<<96) | (h2<<64) | (h3<<32) | h4)[2:]


    return hh

key="test key string"
msg="test message"
#print((SHA1(key+msg)))




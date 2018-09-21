import math
import binascii
import set_1_2

class SHA1:

    def __init__ (self, _h0 = 0x67452301, _h1 = 0xEFCDAB89, _h2 = 0x98BADCFE, _h3 = 0x10325476, _h4 = 0xC3D2E1F0):
        self.h0=_h0
        self.h1=_h1
        self.h2=_h2
        self.h3=_h3
        self.h4=_h4


    def rotl(self, data, rot):
        return ((data << rot) | (data >> (32 - rot))) & 0xffffffff

    def pad(self, unpadded, ml=0):
        if (ml==0):
            ml=len(unpadded)*8
        _pad=unpadded+b"\x80"
        while (len(_pad) % int((512/8)) != int(448/8)):
            _pad += b"\x00"
        _pad+=ml.to_bytes(8, 'big')
        return _pad[len(unpadded):]

    def Hash(self, unprocessed_message, ml=0):
        #initialize values
        h0=self.h0
        h1=self.h1
        h2=self.h2
        h3=self.h3
        h4=self.h4
        #pre_process
        message=unprocessed_message+self.pad(unprocessed_message, ml)
        chunks=[]
        chunk_size=int(512/8)
        num_chunks=math.ceil(len(message)/chunk_size)

        for chunk_count in range(0, num_chunks):
            chunk=(message[chunk_count*chunk_size:(chunk_count+1)*chunk_size])
            words=[]
            word_size=int(32/8)
            for word in range(0,16):
                words.append(int.from_bytes(chunk[word*word_size:(word+1)*word_size], byteorder='big', signed=True))

            for word in range(16, 80):
                new_word=((words[word-3] ^ words[word-8] ^ words[word-14] ^ words[word-16]))
                words.append(self.rotl(new_word, 1))
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



                temp=self.rotl(a, 5) + f + e + k + words[i] & 0xffffffff
                e=d
                d=c
                c=self.rotl(b, 30)
                b=a
                a=temp
            h0= h0 + a & 0xffffffff
            h1= h1 + b & 0xffffffff
            h2= h2 + c & 0xffffffff
            h3= h3 + d & 0xffffffff
            h4= h4 + e & 0xffffffff
        hh=hex((h0<<128) | (h1<<96) | (h2<<64) | (h3<<32) | h4)[2:]


        return hh

#UNCOMMENT BELOW TO RUN CHALLENGE

#key=b""
#msg=b"hello"
#_sha=SHA1()
#print((_sha.Hash(key+msg)))




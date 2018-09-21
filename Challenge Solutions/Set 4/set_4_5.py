import set_4_4 as s4_5
import os
import random

msg="message"

class MAC:
    def __init__(self, key=b""):
        self.key=key

    SHA = s4_5.SHA1()
    def create(self, message):
        return self.SHA.Hash(self.key+message)

    def check(self, message, hash):
        if(self.create(message)==hash):
            print("Token Accepted")
            return True
        else:
            return False

    def check_admin(self, token, hash):
        if self.check(token, hash):
            parsed=self.parsing_routine(token)
            print("Admin Found")
            return(parsed.get(b"admin")==b"true")
        else:
            return False


    def parsing_routine(self, input_string):
        parsed = {}
        if (b';') in input_string:
            element_block = input_string.split(b";")
            for e in range(0, len(element_block)):
                if b'=' in element_block[e]:
                    element_split = element_block[e].split(b"=")
                    parsed[element_split[0]] = element_split[1]
        else:
            raise ValueError("*string is not valid for parsing*")
        return parsed


def length_extension(o_hash, o_message, append_message, _MAC):
    SHA = s4_5.SHA1(int(o_hash[0:8], 16), int(o_hash[8:16], 16), int(o_hash[16:24], 16), int(o_hash[24:32], 16), int(o_hash[32:], 16))
    for key_length in range(0,1000):
        key=key_length*b'A'
        new_ml=len(key+o_message+SHA.pad(key+o_message)+append_message)*8
        new_hash = SHA.Hash(append_message, new_ml)
        new_message=o_message+SHA.pad(key+o_message)+append_message
        if _MAC.check_admin( new_message, new_hash):
            print("MAC Key Length: " + str(key_length))
            break


    return new_message, new_hash

#UNCOMMENT BELOW TO RUN CHALLENGE

MAC1=MAC(os.urandom(random.randint(0, 1000)))
token=b"comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
hashed_token=MAC1.create(token)
length_extension(hashed_token, token, b";admin=true", MAC1)




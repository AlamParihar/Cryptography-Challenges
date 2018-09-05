import set_2_1 as s2_1
import set_3_2 as s3_2
import set_1_2 as s1_2
from crypto.Cipher import AES
import os
import math
import random

def rand_key_gen():
    key=os.urandom(16)
    return key

def pre_append_size_detection(encryption_function):
    no_input=encryption_function(b'')
    with_input=encryption_function(b'a')
    for i in range (0, len(no_input)):
        if no_input[i]!=with_input[i]:
            return i

    return len(no_input)


def parsing_routine(input_string):
    parsed={}
    if (b';') in input_string:
        element_block=input_string.split(b";")
        for e in range(0, len(element_block)):
            if b'=' in element_block[e]:
                element_split=element_block[e].split(b"=")
                parsed[element_split[0]]=element_split[1]
    else:
        raise ValueError ("*string is not valid for parsing*")
    return parsed

unkown_key=rand_key_gen()
unknown_nonce = random.randint(0,2**10)
def CTR_encryption_oracle(user_input):
    prepend=b"comment1=cooking%20MCs;userdata="
    append=b";comment2=%20like%20a%20pound%20of%20bacon;"
    #user_input=user_input.replace(b';', b'').replace(b'=', b'')
    encrypted_string=s3_2.CTR_encrypt(prepend+user_input+append, unkown_key, unknown_nonce)
    return encrypted_string


def check_admin(profile):
    decrypted_string=s3_2.CTR_decrypt(profile, unkown_key, unknown_nonce)
    parsed=parsing_routine(decrypted_string)
    if parsed.get(b"admin")==b"true":
        return 1
    else:
        return 0

def create_admin(user_input):
    pre_append_size=pre_append_size_detection(CTR_encryption_oracle)
    oracle_input=(user_input+"!admin!true").encode()

    oracle_output=CTR_encryption_oracle(oracle_input)
    key_semicolon=s1_2.b16_x(oracle_output[pre_append_size+len(user_input):pre_append_size+len(user_input)+1].hex(), b"!".hex())
    key_equals=s1_2.b16_x(oracle_output[pre_append_size+len(user_input)+6:pre_append_size+len(user_input)+7].hex(), b"!".hex())
    byte_semicolon=bytes.fromhex(s1_2.b16_x(key_semicolon, b";".hex()))
    byte_equals=bytes.fromhex(s1_2.b16_x(key_equals, b"=".hex()))

    admin_profile_token=oracle_output[0:pre_append_size+len(user_input)]+byte_semicolon+oracle_output[pre_append_size+len(user_input)+1:pre_append_size+len(user_input)+6]+byte_equals+oracle_output[pre_append_size+len(user_input)+7:]


    return admin_profile_token


profile=create_admin("FakeName")
if check_admin(profile)==1:
    print("*ADMIN FOUND*")
else:
    print("*ADMIN NOT FOUND*")

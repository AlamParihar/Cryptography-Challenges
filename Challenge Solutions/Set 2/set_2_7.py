import set_2_1 as s2_1
import set_2_2 as s2_2
import set_1_2 as s1_2
from crypto.Cipher import AES
import os
import math


def rand_key_gen():
    key=os.urandom(16)
    return key

def pre_append_size_detection(encryption_function, block_size):
    app_count = 0
    check_block_count = 0
    multiplier = 10
    pre_append_length = 0
    app_size_found = 0

    for a in range (0,16):
        app_test=app_count*'A'+multiplier*'MUTHAFUCKA JONES'
        app_test_result=encryption_function(app_test)
        check_block_prev=""
        for t in range (0,len(app_test_result), block_size):

            check_block=app_test_result[t:t+block_size]
            if check_block==check_block_prev:
                check_block_count+=1
            else:
                check_block_count=1
                input_index=t
            check_block_prev=check_block
            if check_block_count==multiplier:
                pre_append_length= (input_index-app_count)
                app_size_found=1
                return app_count, pre_append_length
        app_count+=1


def block_size_detection(encryption_function):
    block_size_count=0
    cipher_size=encryption_function(b"", unkown_key, IV)
    guess_result_prev = b''
    while (1):
        block_size_count+=1
        block_test_input=block_size_count*'A'
        guess_result=encryption_function(block_test_input.encode(), unkown_key, IV)
        if (block_size_count>1 and len(guess_result)!=len(guess_result_prev)) or (block_size_count>1000):
            found_block_size=abs(len(guess_result)-len(cipher_size))
            break
        guess_result_prev=guess_result
    return found_block_size


def CBC_parsing_routine(input_string):
    parsed={}
    print(input_string)
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
IV =os.urandom(16)
def CBC_encryption_oracle(user_input):
    prepend="comment1=cooking%20MCs;userdata="
    append=";comment2=%20like%20a%20pound%20of%20bacon;"
    user_input=user_input.replace(';','').replace('=', '')
    to_encrypt=s2_1.pad_string_pkcs7((prepend+user_input+append).encode())
    encrypted_string=s2_2.CBC_encrypt(to_encrypt, unkown_key, IV)
    return encrypted_string


def find_admin(decrypted_string):

    parsed=CBC_parsing_routine(decrypted_string)
    if parsed.get(b"admin")==b"true":
        return 1
    else:
        return 0

def create_admin(user_input):
    found_block_size=block_size_detection(s2_2.CBC_encrypt)
    print(pre_append_size_detection(CBC_encryption_oracle, found_block_size))
    admin_string=(b'AadminAtrue').decode()
    fake_string=found_block_size*'A'
    encrypted_string=CBC_encryption_oracle(fake_string+admin_string)
    char_index=2*found_block_size
    encrypted_string = bytearray(encrypted_string)

    encrypted_string[int(char_index)]=int(s1_2.b16_x(hex(encrypted_string[char_index])[2:], s1_2.b16_x(hex(ord('A'))[2:], hex(ord(';'))[2:])), 16)
    char_index+=6
    encrypted_string[int(char_index)] =int(s1_2.b16_x(hex(encrypted_string[char_index])[2:], s1_2.b16_x(hex(ord('A'))[2:], hex(ord('='))[2:])), 16)
    #char_index += 5
    #encrypted_string[int(char_index)] =int(s1_2.b16_x(hex(encrypted_string[char_index])[2:], s1_2.b16_x(hex(ord('A'))[2:], hex(ord(';'))[2:])), 16)
    encrypted_string=bytes(encrypted_string)
    print(encrypted_string)
    decrypted_string=s2_1.pkcs7_unpad(s2_2.CBC_decrypt(encrypted_string, unkown_key, IV))
    print(decrypted_string)

    if find_admin(decrypted_string)==1:
        return "*ADMIN FOUND*"
    else:
        return "*ADMIN NOT FOUND*"



print(create_admin("YELLOW"))
#print(encrypted)
#print(encrypted1)


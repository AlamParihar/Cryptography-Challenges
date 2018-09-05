import base64 as b64
import os
import set_1_2 as s1_2
import set_1_3 as s1_3
import random
import set_2_2 as s2_2
import set_2_1 as s2_1


def block_size_detection(encryption_function, u_key):
    block_size_count=0
    cipher_size=encryption_function(b"", u_key)
    guess_result_prev = b''
    while (1):
        block_size_count+=1
        block_test_input=block_size_count*'A'
        guess_result=encryption_function(block_test_input.encode(), u_key)
        if (block_size_count>1 and len(guess_result)!=len(guess_result_prev)) or (block_size_count>1000):
            found_block_size=abs(len(guess_result)-len(cipher_size))
            break
        guess_result_prev=guess_result
    return found_block_size

def pre_append_size_detection(encryption_function, u_key, block_size):
    app_count = 0
    check_block_count = 0
    multiplier = 20
    pre_append_length = 0
    app_size_found = 0

    for a in range (0,16):
        app_test=app_count*'A'+multiplier*'MUTHAFUCKA JONES'
        app_test_result=encryption_function(app_test.encode(), u_key)
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

def rand_key_gen():
    key=os.urandom(16)
    return key

rand_byte=os.urandom(random.randint(0,20))
def ECB_encryption_oracle(input_string, key):
    app_before=rand_byte
    app_aft=b64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    _unencrypted=app_before+input_string+ app_aft
    to_encrypt=s2_1.pad_string_pkcs7(_unencrypted)
    encrypted_string=s2_2.encrypt_AES_ECB(to_encrypt, key)
    return encrypted_string

def ECB_byte_at_a_time_decryption():
    u_key=rand_key_gen()
    #find block size
    found_block_size=block_size_detection(ECB_encryption_oracle, u_key)
    #pre_append_size
    app_count, pre_append_length=pre_append_size_detection(ECB_encryption_oracle, u_key, found_block_size)
    #decrypt byte by byte
    decrypted_string=""
    orc_input = (app_count+found_block_size - 1) * 'A'
    end_of_string=0
    for b in range (int((pre_append_length+app_count)/16),int(len(ECB_encryption_oracle(b"",u_key))/16)):
        block_string = ""
        for r in range (0,found_block_size):
            test_dict={}
            for char in range(0,255):
                #print(str((orc_input + block_string).encode() + bytes(char)))
                #print((orc_input+block_string +chr(char)).encode())
                test_dict[(ECB_encryption_oracle((orc_input+block_string +chr(char)).encode(), u_key))[pre_append_length+app_count:pre_append_length+app_count+found_block_size]]=chr(char)
            found_char=test_dict.get(ECB_encryption_oracle((orc_input).encode(), u_key)[b*found_block_size:b*found_block_size+found_block_size])
            if found_char == None:
                end_of_string=1
                break
            orc_input = orc_input[1:]
            block_string+=found_char
        decrypted_string+=block_string
        if end_of_string == 1:
            break
        orc_input=app_count*'A'+block_string[1:]

    return decrypted_string

print(ECB_byte_at_a_time_decryption())
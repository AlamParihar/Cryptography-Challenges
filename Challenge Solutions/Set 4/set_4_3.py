import set_2_1 as s2_1
import set_2_2 as s2_2
import set_1_2 as s1_2
from crypto.Cipher import AES
import os
import math


def rand_key_gen():
    key=os.urandom(16)
    return key

def block_size_detection(encryption_function):
    block_size_count=0
    cipher_size=encryption_function(b"")
    guess_result_prev = b''
    while (1):
        block_size_count+=1
        block_test_input=block_size_count*'A'
        guess_result=encryption_function(block_test_input.encode())
        if (block_size_count>1 and len(guess_result)!=len(guess_result_prev)) or (block_size_count>1000):
            found_block_size=abs(len(guess_result)-len(cipher_size))
            break
        guess_result_prev=guess_result
    return found_block_size

unknown_key=b"TEST KEY STRING!"
IV =unknown_key

def CBC_encryption_oracle(user_input):
    to_encrypt=s2_1.pad_string_pkcs7((user_input))
    encrypted_string=s2_2.CBC_encrypt(to_encrypt, unknown_key, IV)
    return encrypted_string

def recieve_token(token):
    decrypted=s2_2.CBC_decrypt(token, unknown_key, IV)
    for i in range(0, len(decrypted)):
        if decrypted[i] > 127:
            return decrypted
            break
    return 1

def recover_key():
    block_size=block_size_detection(CBC_encryption_oracle)
    ciphertext=CBC_encryption_oracle(block_size*3*b"a")
    modded_cipher= ciphertext[0:block_size]+block_size*b"\x00"+ciphertext[0:block_size]
    token_check=recieve_token(modded_cipher)
    if token_check!=1:
        recovered_key=b""
        for i in range(0, block_size):
            recovered_key+=bytes.fromhex(s1_2.b16_x(token_check[i:i+1].hex(), token_check[2*block_size+i:2*block_size+i+1].hex()))
    return recovered_key

print(recover_key())
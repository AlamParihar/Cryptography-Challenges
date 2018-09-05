from crypto.Cipher import AES
import set_1_2 as s1_2
import os
import base64 as b64
import set_2_1 as s2_1
import math

def decrypt_AES_ECB(_encrypted, key):
    de_ciph = AES.new(key, AES.MODE_ECB)
    return de_ciph.decrypt(_encrypted)
def encrypt_AES_ECB(_unencrypted, key):
    en_ciph = AES.new(key, AES.MODE_ECB)
    return en_ciph.encrypt(_unencrypted)

def CBC_decrypt(ciphertext, key, IV):
    ciphertext_blocks=[]
    plaintext_blocks=[]
    next_x=IV.hex()

    for i in range (0, int(math.ceil(len(ciphertext)/16))):
        block=ciphertext[16*i:16*i+16]
        ciphertext_blocks.append(block)
    plaintext_string = b""

    #decrypt CBC block by block
    for b in range (0, len(ciphertext_blocks)):
        dec=decrypt_AES_ECB(ciphertext_blocks[b], key)
        x_or=s1_2.b16_x(dec.hex(), next_x)
        next_x=(ciphertext_blocks[b].hex())
        plaintext_string+=(bytes.fromhex(x_or))
    return plaintext_string

def CBC_encrypt(plaintext_byte_string, key, IV):

    plaintext_blocks = []
    next_x = IV.hex()

    #pad to 16 byte blocks
    for i in range(0, int(math.ceil(len(plaintext_byte_string) / 16))):
        block = s2_1.pkcs7_pad(plaintext_byte_string[16 * i:16 * i + 16], 16)
        plaintext_blocks.append(block)
    encrypted_string=b''

    #encrypt CBC block by block
    for b in range(0, len(plaintext_blocks)):
        x_or=s1_2.b16_x(plaintext_blocks[b].hex(), next_x)
        enc=encrypt_AES_ECB(bytes.fromhex(x_or), key)
        next_x=enc.hex()
        encrypted_string+=enc
    return encrypted_string

###Uncomment below to run challenge###

#with open("c10.txt") as f:
#    codes=""
#    for line in f:
#        codes+=line.strip()
#byte_string=b64.b64decode(codes)
#print(byte_string)

#decoded_message = CBC_decrypt(byte_string, b"YELLOW SUBMARINE", 16*b'0')
#print(decoded_message)


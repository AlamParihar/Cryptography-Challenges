import random
import os
import base64
import set_2_1 as s2_1
import set_2_2 as s2_2
import set_1_2 as s1_2



ukey=os.urandom(16)
IV=os.urandom(16)

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


def u_encrypt_cbc(plain_text):
    padded_plain_text=s2_1.pad_string_pkcs7(plain_text)
    cipher_text=s2_2.CBC_encrypt(padded_plain_text, ukey, IV)
    return cipher_text

def check_padding(in_block):
    pad_length=int(in_block[-1])
    if in_block[-1]<1:
       return 0
    for p in range (len(in_block)-1, len(in_block)-pad_length-1, -1):
        if in_block[p]!=in_block[-1]:
            return 0
    return 1

def padding_oracle(ciphertext):
    plaintext=s2_2.CBC_decrypt(ciphertext, ukey, IV)
    if check_padding(plaintext)==1:
        return 1
    return 0



def padding_attack(cipher_text):

    block_size=block_size_detection(u_encrypt_cbc)
    block_array=[IV]
    plaintext=b''
    plaintext_block=b""
    #plaintext to blocks
    for ind in range (0,(int)(len(cipher_text)/block_size)):
        block_array.append(cipher_text[ind*block_size:(ind+1)*block_size])
    plain = b''
    #loop through blocks
    for block in range (len(block_array)-1,0,-1):
        control=block_size*bytes([0])
        plaintext_block=b''
        #loop through each byte of block
        for _byte in range (block_size-1,-1,-1):
            #loop through all possible guesses
            for b in range (0,256):

                if (_byte<15):
                    control = control[:_byte] + bytes([b]) + control[(_byte+1):]
                else:
                    control = control[:_byte] + bytes([b])

                if padding_oracle(control+block_array[block])==1:
                   
                   break
            #decrypt plaintext byte
            plaintext_byte=bytes.fromhex(s1_2.b16_x(s1_2.b16_x(bytes([block_size-_byte]).hex(), bytes([block_array[block-1][_byte]]).hex()), bytes([b]).hex()))
            plaintext_block=plaintext_byte+plaintext_block
            
            #set coontrol block for next byte guess
            control=control[:_byte]
            for u in range(_byte,block_size):
                controlled_byte=bytes.fromhex(s1_2.b16_x(s1_2.b16_x(bytes([block_size-_byte+1]).hex(), bytes([plaintext_block[u-block_size]]).hex()), bytes([block_array[block-1][u]]).hex()))
                control+=controlled_byte
        #insert solved plaintext block into plaintext string
        plaintext=plaintext_block+plaintext




    return plaintext

string_list=['MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=', 'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=', 'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==','MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==', 'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl', 'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==', 'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==', 'MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=','MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=','MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93']
chosen_string_index=random.randint(0,len(string_list)-1)
chosen_string=string_list[chosen_string_index]
unknown_cipher_text=u_encrypt_cbc(base64.b64decode(chosen_string))
print(padding_attack(unknown_cipher_text))




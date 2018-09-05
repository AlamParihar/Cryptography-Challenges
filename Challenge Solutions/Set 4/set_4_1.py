import set_3_2 as s3_2
import set_1_2 as s1_2
import set_2_2 as s2_2
import os
import random
import base64
u_nonce=random.randint(0,1000)
u_key=os.urandom(16)

with open("c25.txt") as f:
    codes = ""
    for line in f:
        codes += line.strip()
byte_string=base64.b64decode(codes)
unknown_encrypted_text = s3_2.CTR_encrypt(byte_string, u_key, u_nonce)

def Edit_Ciphertext(ciphertext, offset, newtext):
    plaintext=s3_2.CTR_decrypt(ciphertext, u_key, u_nonce)
    edit_plaintext=plaintext[0:offset]+newtext+plaintext[offset+len(newtext):]
    edit_ciphertext=s3_2.CTR_encrypt(edit_plaintext, u_key, u_nonce)
    return edit_ciphertext

#first method, recover each byte (not optimal)
def Break_CTR_Edit_2(unknown_ciphertext):
    recovered_plaintext=b''
    for byte in range(0, len(unknown_ciphertext)):
        edited_ciphertext=Edit_Ciphertext(unknown_ciphertext, byte, b'a')
        for guess in range (0, 256):
            if (bytes.fromhex(s1_2.b16_x(edited_ciphertext[byte:byte+1].hex(), bytes([guess]).hex())) == b'a'):
                recovered_plaintext+=bytes.fromhex(s1_2.b16_x(unknown_ciphertext[byte:byte+1].hex(), bytes([guess]).hex()))
                break

    return recovered_plaintext

#CTR keystream will be xor'd against ciphertext during edit, reproduces plaintext
def Break_CTR_Edit(unknown_ciphertext):
    recovered_plaintext=Edit_Ciphertext(unknown_ciphertext, 0, unknown_ciphertext)
    return recovered_plaintext





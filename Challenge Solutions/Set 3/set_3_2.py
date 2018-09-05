from crypto.Cipher import AES
import math
import base64
import set_1_2 as s1_2

#object for counter
class Counter():
    def __init__(self, bit_size, nonce, endianess):
        self.bits=bit_size
        self.nonce=nonce
        self.endianess=endianess
        self.count=-1
    def update_CTR(self):
        self.count+=1
        count_size_bytes=max(math.ceil(len(bin(self.count)[2:])/8), 1)

        fill=(int(self.bits/8)-count_size_bytes)*bytes([0])
        if self.endianess=='little':
            return (self.nonce).to_bytes(int(self.bits/8), byteorder='little') + (self.count).to_bytes(count_size_bytes, byteorder=self.endianess) +fill
        else:
            return (self.nonce).to_bytes(int(self.bits/8), byteorder='little') + fill + (self.count).to_bytes(count_size_bytes, byteorder=self.endianess)
    def set_new_nonce(self, new_nonce):
        self.nonce=new_nonce


#ENCRYPTION AND DECRYPTION SET TO BLOCK SIZE OF 16
def CTR_encrypt(plaintext, key, nonce):
    ecb_cipher=AES.new(key, AES.MODE_ECB)
    ctr=Counter(64, nonce, 'little')
    encrypted_string=b""
    for i in range(0, len(plaintext)):
        if i%16==0:
            encrypted_ctr = ecb_cipher.encrypt(ctr.update_CTR())
        encrypted_string+=bytes.fromhex(s1_2.b16_x(bytes([plaintext[i]]).hex(), encrypted_ctr[i%16:(i%16)+1].hex()))
    return encrypted_string

def CTR_decrypt(ciphertext, key, nonce):
    ecb_cipher = AES.new(key, AES.MODE_ECB)
    ctr = Counter(64, nonce, 'little')
    decrypted_string = b""
    for i in range(0, len(ciphertext)):
        if i % 16 == 0:
            encrypted_ctr = ecb_cipher.encrypt(ctr.update_CTR())
        decrypted_string += bytes.fromhex(s1_2.b16_x(bytes([ciphertext[i]]).hex(), encrypted_ctr[i % 16:(i % 16) + 1].hex()))
    return decrypted_string

encrypted_string_b64="L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
encrypted_input_string=base64.b64decode(encrypted_string_b64)
decrypted_string=CTR_decrypt(encrypted_input_string, b"YELLOW SUBMARINE", 0)


###Uncomment Below Code To Run Challenge###

#print(decrypted_string)










from crypto.Cipher import AES
import set_1_2 as _2
import base64 as b64


def decrypt_AES_ECB(_encrypted, key):
    de_ciph = AES.new(key, AES.MODE_ECB)
    return de_ciph.decrypt(_encrypted)
def encrypt_AES_ECB(_unencrypted, key):
    en_ciph = AES.new(key, AES.MODE_ECB)
    return en_ciph.encrypt(_unencrypted)

def ascii_encrypt_AES_ECB(_string, key):
    out=encrypt_AES_ECB(_string.encode(), key.encode())
    out=_2.hex2ascii(out.hex())
    return out

def ascii_decrypt_AES_ECB(_string, key):
    out=decrypt_AES_ECB(_string.encode(), key.encode)
    out=_2.hex2ascii(out.hex())
    return out
#f=open("c07.txt", 'r')
#codes=f.read().rstrip()
#byte_string=b64.b64decode(codes)
#decoded_message = decrypt_AES_ECB(byte_string, b"YELLOW SUBMARINE")
#string_="I'm back and I'm ringin' the bell A rockin' on the mike while the fly girls yell In ecstasy in the back of me Well that's my DJ Deshay cuttin' all them Z's Hittin' hard and the girlies goin' crazy Vanilla's on the mike, man I'm not lazy. xx"
#key_=b"YELLOW SUBMARINE"
#print(encrypt_AES_ECB(bytes.fromhex(_2.ascii2hex(string_)), key_))

print(decrypt_AES_ECB(b64.b64decode("rW4q3swEuIOEy8RTIp/DCMdNPtdYopSRXKSLYnX9NQe8z+LMsZ6Mx/x8pwGwofdZ"), b64.b64decode("6v3TyEgjUcQRnWuIhjdTBA==")))





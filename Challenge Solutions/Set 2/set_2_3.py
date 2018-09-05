import base64 as b64
import os
import set_1_2 as s1_2
import set_1_3 as s1_3
import random
import set_2_2 as s2_2
import set_2_1 as s2_1

def encryption_mode_detection(try_string):
    byte_blocks=[]
    check=[]
    for c in range(0,int(len(try_string)/16)):
        byte_blocks.append(try_string[16*c:16*c+16])
    count=0
    for l in range (0, len(byte_blocks)):

        count+=byte_blocks.count(byte_blocks[l])

    count=count/len(byte_blocks)
    if (count>1):
        print("ECB Detected")
        detected = 0
    else:
        print("No ECB Detected")
        detected = 1

    return detected

def rand_key_gen():
    key=os.urandom(16)
    return key

def encryption_oracle(input_string):
    key=rand_key_gen()
    app_bef=os.urandom(random.randint(5,10))
    app_aft=os.urandom(random.randint(5,10))
    _unencrypted= app_bef + input_string + app_aft
    last_block_len=(len(_unencrypted)%16)
    last_block=_unencrypted[-last_block_len:]
    to_encrypt=_unencrypted[:-last_block_len]+s2_1.pkcs7_pad(last_block, 16)
    mode=random.randint(0,1)
    print(mode)
    if mode == 0:
        encrypted_string=s2_2.encrypt_AES_ECB(to_encrypt, key)
    else:
        encrypted_string=s2_2.CBC_encrypt(to_encrypt, key)
    return encrypted_string, mode

#orc_string=40*"This Is A Test String. This is the only string for testing."
#count_ecb=0
#count_cbc=0
#error_cnt=0
#for r in range (0,100):
#    enc_str, enc_mode=encryption_oracle(bytes.fromhex(s1_2.ascii2hex(orc_string)))
#    detected_mode=encryption_mode_detection(enc_str)
#    if detected_mode == 0:
#        count_ecb+=1
#    else:
#        count_cbc+=1
#    if enc_mode != detected_mode:
#        error_cnt+=1
#print("ECB: " + str(count_ecb) + "      CBC: " + str(count_cbc)+"       Error: " +str(error_cnt))


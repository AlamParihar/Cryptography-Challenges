import set_2_4 as s2_4
import set_2_2 as s2_2
import set_2_1 as s2_1
import math

def parsing_routine(input_string):
    parsed_profile={}
    element_block=input_string.split("&")
    for e in range(0, len(element_block)):
        element_split=element_block[e].split("=")
        parsed_profile[element_split[0]]=element_split[1]
    return parsed_profile

def profile_for(user_input, key):

    if type(user_input) == bytes:
        user_input=user_input.decode()
    user_input=user_input.replace('&', '')
    user_input=user_input.replace('=', '')
    UID=10
    role='user'
    profile="email={}&UID={}&role={}".format(user_input, str(UID), role)
    to_encrypt=s2_1.pad_string_pkcs7(profile.encode())
    profile=s2_2.encrypt_AES_ECB(to_encrypt, key)
    return profile

def create_admin_profile():
    u_key=s2_4.rand_key_gen()
    found_block_size=s2_4.block_size_detection(profile_for, u_key)
    fixed_bytes="email=&uid=10&role="
    block_length=(math.ceil(len(fixed_bytes)/found_block_size)*found_block_size)
    email=(block_length-len(fixed_bytes))*'A'
    pre_append=profile_for(email, u_key)[0:block_length]

    fixed_bytes="email="
    block_length =(math.ceil(len(fixed_bytes) / found_block_size) * found_block_size)
    email=(block_length-len(fixed_bytes))*'A'+s2_1.pkcs7_pad(b"admin", found_block_size).decode()
    post_append=profile_for(email, u_key)[block_length:block_length+found_block_size]

    encrypted_profile=pre_append+post_append
    decrypted_profile=s2_2.decrypt_AES_ECB(encrypted_profile, u_key)
    decrypted_profile=s2_1.pkcs7_unpad(decrypted_profile)

    return decrypted_profile

print(parsing_routine(create_admin_profile().decode()))

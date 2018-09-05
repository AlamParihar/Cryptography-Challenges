import set_3_2 as s3_2
import set_1_2 as s1_2
import base64
import math
import os
encrypted_string_list=[]
ukey=os.urandom(16)
nonce=0
with open("set_3_4_input.txt") as f:

    for line in f:
        encrypted_string_list.append(s3_2.CTR_encrypt(base64.b64decode(line), ukey, nonce))

def english_detect(_string):
    #calculate variance of char distribution in string from normal english distribution
    detected=0
    sum=0
    non_letter=0
    freq_error=[]
    total_letters=0
    length=(len(_string))
    freq_english = {b'a': 8.167, b'b': 1.492, b'c': 2.782, b'd': 4.253, b'e': 12.702, b'f': 2.228, b'g': 2.015, b'h': 6.094,
                     b'i': 6.966,
                     b'j': 0.153, b'k': 0.772, b'l': 4.025, b'm': 2.406, b'n': 6.749, b'o': 7.507, b'p': 1.929, b'q': 0.095,
                     b'r': 5.987, b's': 6.327, b't': 9.056,
                     b'u': 2.758, b'v': 0.978, b'w': 2.360, b'x': 0.150, b'y': 1.974, b'z': 0.074, b' ': 18.000}
    #Freq error per letter
    for i in range (65, 91):
        Uppercase=bytes([i])
        Lowercase=bytes([i+32])
        letter_count=(_string.count(Uppercase)+ _string.count(Lowercase))
        total_letters+=letter_count
        letter_freq = letter_count / length
        sum += abs(letter_freq-(freq_english[Lowercase])/100)**2
    #freq error space
    sum+=((_string.count(b' ')/length)-(freq_english[b' ']/100))**2
    #Freq error non-letters
    sum+=abs((length-total_letters)/length-0.08)**2
    #total error for chars in string
    total_error= math.sqrt(sum)
    return total_error

decrypted_strings=[]
for fill in range (0,len(encrypted_string_list)):
    decrypted_strings.append(b"")
min_length=1000000
for _string in encrypted_string_list:
    if len(_string)<min_length:
        min_length=len(_string)



for byte in range (0, min_length):
    error=1
    for guess in range (0, 256):
        decrypted_bytes=b""
        for string in encrypted_string_list:
            encrypted_byte=string[byte:byte+1]
            decrypted_byte=bytes.fromhex(s1_2.b16_x(encrypted_byte.hex(), bytes([guess]).hex()))
            decrypted_bytes+=decrypted_byte
        decrypted_bytes_error=english_detect(decrypted_bytes)
        if (decrypted_bytes_error<error):
            error=decrypted_bytes_error
            solved_bytes=decrypted_bytes
    for _char in range(0, len(solved_bytes)):
        decrypted_strings[_char]+=solved_bytes[_char:_char+1]

print(decrypted_strings)












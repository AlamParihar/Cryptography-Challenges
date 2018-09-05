import set_1_2 as XOR
import math
def english_detect(_string):
    detected=0
    sum=0
    non_letter=0
    freq_error=[]
    freq_english = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094,
                     'i': 6.966,
                     'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095,
                     'r': 5.987, 's': 6.327, 't': 9.056,
                     'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074, ' ': 18.000}
    for i in range (0, 127):
        letter=str(chr(i))
        if letter in freq_english:
            letter_freq = _string.count(letter) / len(_string)
            sum += abs(letter_freq-(freq_english[letter])/100)**2
        else:
            non_letter+=_string.count(letter)
    sum+=abs(non_letter/len(_string)-0.08)**2

    total_error= math.sqrt(sum)
    return total_error


def brute_force_decrypt(str1):
    min_error=100
    found_message=""
    found_key=""
    found_error=""
    for i in range (0,126):
        cipher_key=hex(int(i))
        key_string=int(len(str1))*cipher_key[2:]


        decoded_hex=XOR.b16_x(str1, key_string)
        decrypted_string=''
        for c in range (0, int(len(decoded_hex)),2):
            decrypted_string+=chr(int(decoded_hex[c:c+2], 16))
        error=english_detect(decrypted_string)
        if (error<min_error):
            #print("key:" + chr(i), ",   Decrypted Message:" + decrypted_string, ",Error:" + str(error))
            found_message=(decrypted_string)
            found_key=(chr(i))
            found_error=(error)
            min_error=error
    return (found_key, found_message, found_error)


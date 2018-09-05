import  math
import set_1_2 as XOR


def encrypt_string(input_string, key):
    key_ascii_string=math.ceil(len(input_string)/len(key))*key
    encrypted_string=""
    input_hex=""
    key_string=""
    for i in range (0, len(input_string)):
        input_hex_string="0x%x" % ord(input_string[i])
        input_hex += input_hex_string[2:4]
        key_hex_string="0x%x" % ord(key_ascii_string[i])
        key_string+=key_hex_string[2:4]
    encoded_hex=XOR.b16_x(input_hex, key_string)
    for c in range(0, int(len(encoded_hex)), 2):
        encrypted_string += chr(int(encoded_hex[c:c + 2], 16))
    return encoded_hex

print(encrypt_string("I be tossin, enforcin, my style is awesome I'm causin more Family Feud's than Richard Dawson And the survey said -- ya dead Fatal Flying Guillotine chops off your fuckin head MZA who was that? Aiyyo, the Wu is back Makin niggaz go BO BO!, like on Super Cat Me fear no-one, oh no, here come The Wu-Tang shogun, killer to the eardrum! I puts the needle to the groove, I gets rude And I'm forced to fuck it up My style carries like a pickup truck Across the clear blue yonder Seek the China Sea, I slam tracks like quarterbacks sacks from L.T. Now why try and test, the Rebel INS? Blessed since the birth, I earth-slam your best Cause I bake the cake, then take the cake and eat it, too, with my crew while we head state to state!", "Wu-Tang Clan Ain't Nuthing Ta Fuck Wit"))


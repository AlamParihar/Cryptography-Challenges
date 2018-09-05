import set_1_3 as rep
import set_1_2 as XOR
import set_1_1 as _1


def hextoascii(_input):
    ascii_string=""
    for c in range(0, int(len(_input)), 2):
        ascii_string += chr(int(_input[c:c + 2], 16))
    return ascii_string

def bin_8bit(var):
    out_bit_array=""
    for z in range(0, 8):
        _bit = int(var % 2)
        var = int(var / 2)
        out_bit_array += str(_bit)
    out_1 = out_bit_array[::-1]
    return out_1

#ascii input
def Hamming_Distance(str1, str2):
    #ascii to hex
    distance=0
    letter1_bin=""
    letter2_bin=""

    for i in range (0,max(len(str1),len(str2)),2):
        letter_1='{0:08b}'.format(int(str1[i:i+2], 16))
        letter_2='{0:08b}'.format(int(str2[i:i+2], 16))
        letter1_bin+=letter_1
        letter2_bin+=letter_2
    for b in range (0,min(len(letter1_bin), len(letter2_bin))):
        distance += (int(letter1_bin[b]) ^ int(letter2_bin[b]))

    return distance

def key_size_test(_input):
    min_dist=2^16
    key_size=0
    results=[]
    for i in range (2,41,1):
        str1=_input[0:2*i]
        str2=_input[2*i:4*i]
        str3=_input[4*i:6*i]
        str4=_input[6*i:8*i]
        str5=_input[8*i:10*i]
        str6=_input[10*i:12*i]
        dist=((Hamming_Distance(str1, str2))+(Hamming_Distance(str1, str3))+Hamming_Distance(str1,str4)+ Hamming_Distance(str1,str5)+Hamming_Distance(str1,str6)+Hamming_Distance(str2,str3)+Hamming_Distance(str2,str4)+Hamming_Distance(str2,str5)+Hamming_Distance(str2,str6)+Hamming_Distance(str3,str4)+Hamming_Distance(str3,str5)+Hamming_Distance(str3,str6)+Hamming_Distance(str4,str5)+Hamming_Distance(str4,str6)+Hamming_Distance(str5,str6))/(5*4*3*2*i)
        results.append(((dist), i))
    results.sort(key=lambda x: x[0])
   # for z in range (0, len(results)):
    #    print(results[z][0], results[z][1])
    return results

def decrypt_repeating_key(_input):
    test_results=key_size_test(_input)
    found_messages=[]
    #use 3 best key sizes
    for z in range (0,5):
        key_size=test_results[z][1]
        key_string=""
        decrypted_string=""
        #transpose blocks of key size by byte
        for i in range(0, key_size):
            block=""
            for j in range(2*i,len(_input),2*key_size):
                block+=str(_input[j]+_input[j+1])
            (key, message, error) = rep.brute_force_decrypt(block)

            key_string+=key
        key_hex=XOR.ascii2hex(int(len(_input))*(key_string))

        decoded_hex=XOR.b16_x(_input, key_hex)
        #conversion from hex to ascii
        for c in range(0, int(len(decoded_hex)), 2):
            decrypted_string += chr(int(decoded_hex[c:c + 2], 16))
        found_messages.append((rep.english_detect(decrypted_string), decrypted_string, key_string))
    found_messages.sort(key=lambda x: x[0])
    return (found_messages[0][1], found_messages[0][2])

with open("b64.txt") as codes:
     count = 0
     _b64=""
     for line in codes:
         _b64+=line.strip()
encoded_string=_1.b642hex(_b64[0:len(_b64)-1])

#encoded_string="1e554f31411a085330050f4200240708480643271b58480417475320184c23550a1800361e11241a40314127404d630f001b5328074e4a1b522b55320904070b59742745331144180023011539557f3d02060652274c250f5732060007354e2a5500000c4e14552617453f55100a493349597a555435410a0241274c270f5420054e611859271b13482e1b0e4c380e542f1b064b433f060424554232074e1e4f361e4108552202074954482b1410482434260023094f6602021800230115234a0d1508171e4f6f4c150645613e1b071d536e17150b024e2a413f084e661b0a0c47361354301a0d162e4e256f62404102492a0c4e481a001d00040d1b4e244120416d2355050e4125491a3858423a0442474f2b4c0f010c61010b5511002d1a190d493a0f457436556b21020547771a1c3812583a4d4e0c492f00041c0035064e531c456e10151a0d1c124d7541696605161f53771d1c32554331040a0b4563180e4e54290c4e40064f21031144492747473115536607160f4577281a335564730c4e014f310f040a0035064e41014325551d1c491b170019180035011a0745770a1525074431124e0b492809410f0031000d4c01506e01061d0a05476137134f3506431f483249173b104c26410c0b55264c18014e250c1c0727452b1e541c010b47633c084e2755300e417b493d770641350c4e1352220f0a1d002d00054254513b14061c0c1c0541370a53660602084b244912251a40742d40330e63220e1900360117070052375515060d4e134527150c66010b0e00050c1632190d1d2f3d58000100041d53240d4e541d4e2d10541c010b47423d13542e59432200320806231d00270d0f0a003a03141c00230c1d5354632f00070d49274742350a4566010b0e0034081f32590d20090b0900370d0a0b0035010b07174125105409070a47453515002f014f4b5438065877024420094e0a59630f130b57611e064e18456e021148010b06447412542701064b543849072314593140"

(r_message, r_key)=decrypt_repeating_key(encoded_string)
print("Message: " + r_message)
print("Key=      " + r_key)



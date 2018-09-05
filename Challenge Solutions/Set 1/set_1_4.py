import set_1_3 as rep
with open("Codes.txt") as codes:
    count=0
    for line in codes:
        (key, message, error)=rep.brute_force_decrypt(line.strip())
        if len(message) !=0 :
            print("key:" + key[0] + ",   Decrypted Message:" + message[0] + ",   Line:" + str(count))
        count+=1
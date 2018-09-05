import set_1_2 as _2


def detect_ECB(file_name):
    f=open(file_name, 'r')
    check=[]
    line_num=0
    for line in f.readlines():

        try_string=bytes.fromhex("d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a")
        byte_blocks=[]
        for c in range(0,int(len(try_string)/16)):
            byte_blocks.append(try_string[16*c:16*c+16])
        count=0
        for l in range (0, len(byte_blocks)):

            count+=byte_blocks.count(byte_blocks[l])
        count=count/len(byte_blocks)
        if (count>1):
            check.append((count, line_num,))
        line_num += 1
    if (len(check)==0):
        print("No ECB Detected")
    else:
        check.sort(key=lambda x: x[0])

    return check

#ff='c08.txt'
#ans=detect_ECB(ff)
#for z in range(0, len(ans)):
#    print("ECB Detected, Line"+ str(ans[z][1]))

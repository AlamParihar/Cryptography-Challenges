def pkcs7_pad(in_block, out_block_size):
    diff=int(out_block_size)-len(in_block)
    if diff > 0:
        append=diff*(bytes([diff]))
        out_block=in_block+append
        return out_block
    else:
        return in_block

def pkcs7_unpad(in_block):
    pad_length=int(in_block[-1])
    for p in range (len(in_block)-1, len(in_block)-pad_length-1, -1):
        if in_block[p]!=in_block[-1]:
            raise ValueError('*NOT VALID PKCS7 PADDING*')
            return in_block
    return in_block[0:len(in_block)-pad_length]

def pad_string_pkcs7(input_string):
    last_block_len=(len(input_string)%16)
    last_block=input_string[-last_block_len:]
    padded_string=input_string[:-last_block_len]+pkcs7_pad(last_block, 16)
    return padded_string

def unpad_string_pkcs7(input_string, block_size):
    last_block = input_string[-block_size:]
    unpadded_string = input_string[:len(input_string)-block_size]+pkcs7_unpad(last_block)
    return unpadded_string


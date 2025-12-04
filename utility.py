def bin2int(b):
    total = 0
    for i in range(len(b)):
        total += int(b[-i-1])*(2**i)
    return total

def int2bin(int_num, bit_length): 
    bits = bin(int_num).replace("0b", "")
    return f"{"0"*(bit_length-len(bits))}{bits}"


def flip_bit(bit_str, bit_index):
    '''
    Flips a bit within `bit_str` at the specified `bit_index`\n
    *Example:* 
    
    `flip_bit("0010", 0) -> "1010"`
    '''
    temp = list(bit_str)
    temp[bit_index] = str(int(bit_str[bit_index] == "0")) # flip bit at b
    n_bin_pos = "".join(temp)   # join temp list into string
    return n_bin_pos



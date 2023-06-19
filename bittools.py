def to_bits(numb):
    tmp=[]
    while len(tmp)<8:
        numb,bit = divmod(numb,2)
        tmp.append(bit)
    tmp = tmp[::-1]
    return tmp

def to_bytes(lst):
    tmp=[]
    for i in range(0,len(lst),8):
        bt = lst[i:i+8]
        bnumb = 0
        for k,e in enumerate(bt):
            bnumb += 2**(7-k) * e
        tmp.append(bnumb)
    return bytes(tmp)
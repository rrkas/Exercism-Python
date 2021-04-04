SUBLIST = 'a in b'
SUPERLIST = 'b in a'
EQUAL = 'a = b'
UNEQUAL = 'a <> b'


def sublist(a: list, b: list):
    if a == b:
        return EQUAL
    if len(a) == len(b):
        return UNEQUAL
    la = len(a)
    lb = len(b)
    if la > lb:
        if any([b == a[i:i+lb] for i in range(la-lb+1)]):
            return SUPERLIST
        return UNEQUAL
    else:
        if any([a == b[i:i+la] for i in range(lb-la+1)]):
            return SUBLIST
        return UNEQUAL

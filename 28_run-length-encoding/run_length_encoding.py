def decode(string):
    s = ''
    ctr = ''
    if string != "":
        for i in string:
            if i in "1234567890":
                ctr += i
            else:
                if ctr == '':
                    s += i
                else:
                    s += (int(ctr) * i)
                    ctr = ''
            # print(string, s, ctr, i)
    return s


def encode(string):
    s = ''
    c = ''
    ctr = 0
    if string != "":
        for i in string:
            if i == c:
                ctr += 1
            else:
                if ctr > 1:
                    s += str(ctr) + c
                else:
                    s += c
                c = i
                ctr = 1
    if ctr > 1:
        s += str(ctr) + c
    else:
        s += c
    return s


# print(decode("12WB12W3B24WB"))
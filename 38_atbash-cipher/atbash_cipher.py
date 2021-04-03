org = 'abcdefghijklmnopqrstuvwxyz'
rev = org[::-1]
nums = '1234567890'


def encode(plain_text):
    s = ''
    for c in plain_text:
        if c.lower() in org:
            s += rev[org.index(c.lower())]
        elif c in nums:
            s += c
    return ' '.join([ s[i:min(i+5, len(s))] for i in range(0, len(s), 5) ])


def decode(ciphered_text):
    s = ''
    for c in ciphered_text:
        if c.lower() in org:
            s += org[rev.index(c.lower())]
        elif c in nums:
            s += c
    return s

from math import ceil, sqrt


def cipher_text(plain_text: str):
    pt = "".join(filter(str.isalnum, plain_text.lower()))
    if not pt: return ""
    l, c = len(pt), ceil(sqrt(len(pt)))
    if l % c:
        pt += " " * (c - l % c)
    return " ".join(pt[i::c] for i in range(c))
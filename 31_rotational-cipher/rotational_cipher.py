abc = 'abcdefghijklmnopqrstuvwxyz'


def rotate(text, key):
    cipher = abc[key:] + abc[:key]
    ciphered_text = ''
    for c in text:
        if c in [' ', "'", ',', '.', '!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            ciphered_text += c
        else:
            for ctr, i in enumerate(abc):
                if c == i:
                    ciphered_text += cipher[ctr]
                elif c == i.upper():
                    ciphered_text += cipher.upper()[ctr]
    return ciphered_text
def is_pangram(sentence):
    for i in range(26):
        if str(chr(65+i)) not in sentence.upper():
            return False
    return True

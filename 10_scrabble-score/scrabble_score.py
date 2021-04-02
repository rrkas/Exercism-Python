def score(word):
    s = 0
    for c in word.upper():
        if c in "AEIOULNRST":
            s = s + 1
        elif c in "DG":
            s = s + 2
        elif c in "BCMP":
            s = s + 3
        elif c in "FHVWY":
            s = s + 4
        elif c == "K":
            s = s + 5
        elif c in "JX":
            s = s + 8
        elif c in "QZ":
            s = s + 10
    return s
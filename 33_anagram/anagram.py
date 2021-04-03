def find_anagrams(word, candidates):
    s = []
    for c in candidates:
        if c.upper() == word.upper():
            continue
        if len(word) == len(c):
            chs = list(set([i for i in c]))
            if [word.upper().count(i.upper()) for i in chs] != [c.upper().count(i.upper()) for i in chs]:
                continue
            s.append(c)
    return s

def abbreviate(string):
    s = ""
    for w in string.split(" "):
        if w[0] == '_':
            s = s + w[1]
        elif w != '-':
            for w_ in w.split('-'):
                s = s + w_[0]
    return s.upper()

def translate(text):
    if len(text.split()) > 1:
        s = []
        for word in text.split():
            s.append(translate(word))
        return ' '.join(s)

    s = ''
    if text[0] in 'aeiou' or text[:2] in ['xr', 'yt']:
        s = text + 'ay'
    else:
        cc = text[0]    # consonant cluster
        i = 1
        while text[i] not in 'aeiouy':
            cc += text[i]
            i += 1
        if cc[-1] == 'q' and text[i] == 'u':
            s = text[i + 1:] + cc + 'uay'
        else:
            s = text[i:] + cc + 'ay'

    return s

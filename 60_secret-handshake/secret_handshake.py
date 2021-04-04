map = {
    1: 'wink',
    2: 'double blink',
    4: 'close your eyes',
    8: 'jump',
}


def commands(n: int) -> list:
    s = []
    for k,v in map.items():
        if n&k:
            s.append(v)
    if n&16:
        s.reverse()
    return s

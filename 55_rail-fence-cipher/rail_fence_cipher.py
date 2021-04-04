def encode(message: str, rails: int) -> str:
    rail_slots = [[] for i in range(rails)]
    chs = [i for i in message if i.isalnum()]
    r_idx = 0
    for i in chs:
        if r_idx == 0:
            direction = 1
        elif r_idx == rails - 1:
            direction = -1
        rail_slots[r_idx].append(i)
        r_idx += direction
    s = ''
    for i in rail_slots:
        s += ''.join(i)
    return s


def decode(encoded_message: str, rails: int) -> str:
    rail_slots = [[] for i in range(rails)]
    chs = list(encoded_message)
    count = {i: 0 for i in range(rails)} # counts number of chs in each rail
    rail = 0
    for i in range(len(chs)):
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        count[rail] += 1
        rail += direction
    j = 0
    for i in range(rails):
        rail_slots[i].extend(chs[j:j + count[i]])
        j += count[i]
    s = ''
    rail = 0
    for i in range(len(chs)):
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = - 1
        s += rail_slots[rail].pop(0)
        rail += direction
    return s

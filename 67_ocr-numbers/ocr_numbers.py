from typing import List

map = {
    0: [' _ ', '| |', '|_|', '   '],
    1: ['   ', '  |', '  |', '   '],
    2: [' _ ', ' _|', '|_ ', '   '],
    3: [' _ ', ' _|', ' _|', '   '],
    4: ['   ', '|_|', '  |', '   '],
    5: [' _ ', '|_ ', ' _|', '   '],
    6: [' _ ', '|_ ', '|_|', '   '],
    7: [' _ ', '  |', '  |', '   '],
    8: [' _ ', '|_|', '|_|', '   '],
    9: [' _ ', '|_|', ' _|', '   '],
    10: [' _ ', '| |', '|_|', '   '],
}


def convert(input_grid: List[str]) -> str:
    if any(len(i) % 3 != 0 for i in input_grid) or len(input_grid) % 4 != 0:
        raise ValueError(' ')
    n = ''
    for l in range(0, len(input_grid), 4):
        for i in range(0, len(input_grid[l: l+4][0]), 3):
            t = []
            for j in range(4):
                t.append(input_grid[j + l][i: i+3])
            if t not in map.values():
                n += '?'
            else:
                n += str(list(map.keys())[list(map.values()).index(t)])
        n += ','
    return n if len(input_grid) == 4 else n[:-1]

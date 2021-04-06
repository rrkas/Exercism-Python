def transpose(lines: str) -> str:
    l = lines.replace(' ', '*').split('\n')
    m = max(len(i) for i in l)
    t = [''] * m
    for i in range(len(l)):
        for j in range(m):
            if len(l[i]) > j:
                t[j] += l[i][j]
            else:
                t[j] += ' '
    for i in range(len(t)):
        t[i] = t[i].rstrip()
    return '\n'.join(t).replace('*', ' ')


if __name__ == '__main__':
    lines = ["The longest line.", "A long line.", "A longer line.", "A line."]
    print('\n'.join(lines))
    print(transpose('\n'.join(lines)))
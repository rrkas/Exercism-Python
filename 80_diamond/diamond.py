def rows(letter):
    fill = ' '
    s = []
    lc = 2 * (ord(letter) - ord('A')) + 1
    for i in range(lc):
        l = ''
        if i in (0, lc - 1):
            l += fill * (lc//2)
            l += 'A'
            l += fill * (lc//2)
        elif i <= lc//2:
            d = chr(ord('A') + i)
            l += fill * (lc//2 - i)
            l += d
            l += fill * (2*(i-1)+1)
            l += d
            l += fill * (lc // 2 - i)
        else:
            dif = i - lc//2
            d = chr(ord(d) - 1)
            l += fill * dif
            l += d
            l += fill * (lc - 2*len(l))
            l += d
            l += fill * dif
        s.append(l)
    return s


if __name__ == '__main__':
    for i in rows('D'):
        print(i)
from math import floor


def triplets_with_sum(n):
    s = []
    for i in range(n // 3):
        for j in range(i+1, n // 2):
            k = (i**2 + j**2)**0.5
            print(k, int(k), k%1)
            if i + j + int(k) == n and k%1==0:
                t = [j, i, int(k)]
                t.sort()
                s.append(t)
    return s


if __name__ == '__main__':
    print(triplets_with_sum(1001))

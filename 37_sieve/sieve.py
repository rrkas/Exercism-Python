def primes(limit):
    s = list(range(2, limit+1))
    for i in s:
        for j in range(2, len(s)):
            if i * j > s[-1]:
                break
            if i * j in s:
                s.remove(i * j)
    return s

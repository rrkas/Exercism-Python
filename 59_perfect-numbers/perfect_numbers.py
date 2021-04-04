def classify(n: int) -> str:
    if n < 1:
        raise ValueError(' ')
    s = 0
    for i in range(1, n):
        if n%i == 0:
            s += i
    if s == n:
        return "perfect"
    elif s > n:
        return "abundant"
    else:
        return 'deficient'

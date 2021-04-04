from math import ceil


def prime(n: int) -> int:
    if n<1:
        raise ValueError(' ')
    ctr = 0
    i = 2
    while ctr < n:
        if is_prime(i):
            ctr += 1
        i += 1
    return i-1


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i += 2
    return True
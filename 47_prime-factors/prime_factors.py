def factors(value: int) -> list:
    n = value
    s = []
    for i in generate_primes(value):
        while n % i == 0:
            s.append(i)
            n //= i
        if n == 1:
            break
    return s


def generate_primes(n: int):
    for i in range(2, n+1):
        if is_prime(i):
            yield i


def is_prime(n: int):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i <= n ** 0.5:
            if n % i == 0:
                return False
            i += 2
        return True

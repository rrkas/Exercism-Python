def largest(min_factor: int, max_factor: int) -> (int, list):
    if min_factor == max_factor:
        return None, []
    if min_factor > max_factor:
        raise ValueError(' ')
    m = 0
    f = []
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            if is_palindrome(i*j):
                if m < i * j:
                    m = i * j
                    f = [[i, j]]
                elif m == i * j:
                    f.append([i, j])
    return m, f


def smallest(min_factor: int, max_factor: int):
    if min_factor == max_factor:
        return None, []
    if min_factor > max_factor:
        raise ValueError(' ')
    m = None
    f = []
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            if is_palindrome(i * j):
                if m is None:
                    m = i * j
                    f = [[i, j]]
                else:
                    if m > i*j:
                        m = i * j
                        f =[[i, j]]
                    elif m == i*j:
                        f.append([i, j])
    return m, f


def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


# def factors(n: int) -> list:
#     s = []
#     if n is None:
#         return s
#     for i in range(2,n//2):
#         if n % i == 0:
#             s.append(list(sorted([i, n//i])))
#     return s


if __name__ == '__main__':
    print(smallest(min_factor=1002, max_factor=1003))
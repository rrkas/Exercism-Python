def sum_of_multiples(limit, multiples):
    s = 0
    for i in range(1, limit):
        for j in multiples:
            if j and i % j == 0:
                s += i
                break
    return s

def square(number):
    if number < 1 or number > 64:
        raise ValueError('ValueError')
    return 2 ** (number - 1)


def total():
    return sum([square(i) for i in range(1, 65)])

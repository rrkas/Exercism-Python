def is_armstrong_number(number: int) -> bool:
    p = len(str(number))
    s = 0
    for ds in str(number):
        d = int(ds)
        s += d**p
    return s == number

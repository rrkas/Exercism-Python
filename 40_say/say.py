NUMBERS = {
    0: "zero",      1: "one",           2: "two",           3: "three",
    4: "four",      5: "five",          6: "six",           7: "seven",
    8: "eight",     9: "nine",          10: "ten",          11: "eleven",
    12: "twelve",   13: "thirteen",     14: "fourteen",     15: "fifteen",
    16: "sixteen",  17: "seventeen",    18: "eighteen",     19: "nineteen",
    20: "twenty",   30: "thirty",       40: "forty",        50: "fifty",
    60: "sixty",    70: "seventy",      80: "eighty",       90: "ninety",
    100: "hundred", 1000: "thousand",   1000_000: "million",1000_000_000: "billion"
}


def say(number):
    r = 0
    sep = " "
    if number < 0:
        raise ValueError("Number must be positive")
    elif number < 21:
        s = NUMBERS[number]
    elif number < 100:
        s = NUMBERS[int(number/10)*10]
        r = number % 10
        sep = "-"
    elif number < 1000:
        s = NUMBERS[int(number/100)] + sep + NUMBERS[100]
        r = number % 100
    elif number < 1000000:
        s = say(int(number/1000)) + sep + NUMBERS[1000]
        r = number % 1000
    elif number < 1000000000:
        s = say(int(number/1000000)) + sep + NUMBERS[1000000]
        r = number % 1000000
    elif number < 1000000000000:
        s = say(int(number/1000000000)) + sep + NUMBERS[1000000000]
        r = number % 1000000000
    else:
        raise ValueError("Value must not be greater than 999999999999")
    if r > 0:
        s += sep + say(r)
    return s
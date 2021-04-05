def equilateral(sides: list) -> bool:
    un = set(sides)
    if len(un) == 1 and not (0 in un) and is_triangle(sides):
        return True
    return False


def isosceles(sides: list) -> bool:
    un = set(sides)
    if len(un) <= 2 and not (0 in un) and is_triangle(sides):
        return True
    return False


def scalene(sides: list) -> bool:
    un = set(sides)
    if len(un) == 3 and not (0 in un) and is_triangle(sides):
        return True
    return False


def is_triangle(sides: list) -> bool:
    if len(sides) < 3:
        return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a+b>c and a+c>b and b+c>a

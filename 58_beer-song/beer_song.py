def recite(start, take=1):
    if start == 0:
        return [
            "No more bottles of beer on the wall, no more bottles of beer.",
            "Go to the store and buy some more, 99 bottles of beer on the wall.",
        ]
    elif start == 1:
        return [
            "1 bottle of beer on the wall, 1 bottle of beer.",
            "Take it down and pass it around, no more bottles of beer on the wall.",
        ]
    elif take == 1:
        return [
            "{} bottle{} of beer on the wall, {} bottle{} of beer.".format(start, 's' if start > 1 else '', start, 's' if start > 1 else ''),
            "Take one down and pass it around, %s bottle%s of beer on the wall." % (start-1, 's' if start-1 > 1 else ''),
        ]
    else:
        s = []
        s.extend(recite(start))
        take -= 1
        start -= 1
        while start >= 0 and take > 0:
            s.append("")
            s.extend(recite(start))
            start -= 1
            take -= 1
        return s


if __name__ == '__main__':
    for i in recite(start=99, take=100):
        print(i)
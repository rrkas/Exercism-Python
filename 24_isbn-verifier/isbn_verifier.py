def is_valid(isbn):
    isbn = isbn.replace("-","")
    if len(isbn) != 10:
        return False
    s = 0
    for i in range(len(isbn)):
        try:
            s += (10-i) * int(isbn[i])
        except:
            if isbn[i] == "X":
                s += 10
            else:
                return False
    return s % 11 == 0

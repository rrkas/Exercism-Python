def append(list1, list2):
    list1.extend(list2)
    return list1


def concat(lists):
    s = []
    for e in lists:
        if isinstance(e, list):
            s.extend(e)
        else:
            s.append(e)
    return s


def filter(function, list):
    return [e for e in list if function(e)]


def length(list):
    return len(list)


def map(function, list):
    return [function(e) for e in list]


def foldl(function, list, initial):
    r = initial
    for e in list:
        r = function(r, e)
    return r


def foldr(function, list, initial):
    r = initial
    for e in list[::-1]:
        r = function(e, r)
    return r


def reverse(list):
    return list[::-1]

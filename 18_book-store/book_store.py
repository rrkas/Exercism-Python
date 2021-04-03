def total(basket):
    sets = []
    while len(basket):
        uniques = set(basket)
        sets.append(len(uniques))
        for e in uniques:
            basket.remove(e)
    #2 sets of 4 are cheaper than a set of 3 and a set of 5
    while 3 in sets and 5 in sets:
        sets.remove(3)
        sets.remove(5)
        sets += [4, 4]
    dicounts = [1, .95, .9, .8, .75]
    return sum([i*dicounts[i-1]*800 for i in sets])
    
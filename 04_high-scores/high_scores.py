def latest(scores):
    return scores[-1]


def personal_best(scores):
    return list(sorted(scores))[-1]


def personal_top_three(scores):
    l = list(reversed(list(sorted(scores))))

    return [ l[i] for i in range(min(3,len(l)))]


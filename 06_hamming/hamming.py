def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("ValueError")
    l = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            l = l + 1
    return l
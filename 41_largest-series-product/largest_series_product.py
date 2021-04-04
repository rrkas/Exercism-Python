def largest_product(series: str, size: int) -> int:
    if size > len(series) or size < 0:
        raise ValueError('ValueError')
    if series == '' or size == 0:
        return 1
    m = 0
    for g in range(len(series) - size + 1):
        n = series[g:g+size]
        t = 1
        for d in n:
            t *= int(d)
        if t > m:
            m = t
    return m

def find(search_list, value: int) -> int:
    if len(search_list) == 0:
        raise ValueError(' ')
    l = 0
    r = len(search_list) - 1
    while l <= r:
        m = l + (r - l)//2
        if value == search_list[m]:
            return m
        elif value > search_list[m]:
            l = m + 1
        else:
            r = m - 1
    raise ValueError(' ')

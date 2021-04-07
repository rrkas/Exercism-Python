def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError(' ')
    s = 0
    for d in digits:
        if d >= input_base or d<0:
            raise ValueError(' ')
        s = s*input_base + d
    r = []
    if not s:
        return [0]
    while s:
        d = s%output_base
        r.append(d)
        s //= output_base
    return r[::-1]

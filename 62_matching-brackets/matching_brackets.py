def is_paired(input_string) -> bool:
    s = []
    opening = ('(', '{', '[')
    closing = (')', '}', ']')
    for i in input_string:
        try:
            if i in opening:
                s.append(i)
            elif i in closing:
                if s.pop() != opening[closing.index(i)]:
                    return False
        except:
            return False
    if len(s):
        return False
    return True

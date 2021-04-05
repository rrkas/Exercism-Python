def answer(question: str) -> int:
    words = question[8:-1].split()
    operators = ["multiplied", "divided", "plus", "minus"]
    for i in range(words.count('by')):
        words.remove('by')
    result = None
    while words:
        if result is None:
            result = int(words[0])
            del words[0]
        if words:
            if words[0] in operators:
                try:
                    if words[0] == operators[0]:
                        result *= int(words[1])
                    elif words[0] == operators[1]:
                        result /= int(words[1])
                    elif words[0] == operators[2]:
                        result += int(words[1])
                    elif words[0] == operators[3]:
                        result -= int(words[1])
                    del words[0:2]
                except IndexError:
                    raise ValueError(' ')
            elif words[0] not in operators:
                words.remove(words[0])
                raise ValueError(' ')
    if result is not None:
        return result
    else:
        raise ValueError("missing operand")
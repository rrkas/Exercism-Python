from typing import List


def flatten(iterable: List) -> List[int]:
    s = []
    for e in iterable:
        if isinstance(e, list):
            s.extend(flatten(e))
        elif e is not None:
            s.append(e)
    return s

import collections


def transform(legacy_data: dict) -> dict:
    s = {}
    for k,v in legacy_data.items():
        for e in v:
            s[e.lower()] = k
    return collections.OrderedDict(s.items())

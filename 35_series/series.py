from typing import List


def slices(series: str, length: int) -> List[str]:
    if length > len(series) or series == '' or length < 1:
        raise ValueError('ValueError')
    return [series[i:i+length] for i in range(len(series) - length + 1)]

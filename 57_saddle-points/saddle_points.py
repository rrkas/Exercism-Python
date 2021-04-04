from typing import List


def saddle_points(matrix: List[List[int]]) -> List[dict]:
    if any(len(matrix[0]) != len(matrix[i]) for i in range(len(matrix))):
        raise ValueError(' ')
    s: List[dict] = []
    for r_idx in range(len(matrix)):
        for c_idx in range(len(matrix[0])):
            r = max(matrix[r_idx])
            c = min([matrix[i][c_idx] for i in range(len(matrix))])
            e = matrix[r_idx][c_idx]
            if r == c == e:
                s.append({'row': r_idx+1, 'column': c_idx+1})
    return s
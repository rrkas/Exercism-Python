from typing import List


def annotate(minefield: List[str]) -> List[str]:
    if len(minefield) == 0:
        return minefield
    if any(len(minefield[0]) != len(minefield[i]) for i in range(len(minefield))):
        raise ValueError(' ')
    r = len(minefield)
    c = len(minefield[0])
    for i in range(r):
        for j in range(c):
            if minefield[i][j] not in ('*', ' '):
                raise ValueError(' ')
            elif minefield[i][j] == ' ':
                ctr: int = get_surr(minefield, i, j).count('*')
                if ctr:
                    minefield[i] = minefield[i][:j] + str(ctr) + minefield[i][j+1:]
                else:
                    minefield[i] = minefield[i][:j] + ' ' + minefield[i][j + 1:]
    return minefield


def get_surr(mat: List[str], i: int, j: int) -> list:
    s = []
    r = len(mat)
    c = len(mat[0])
    if i:
        if j:
            s.append(mat[i - 1][j - 1])
        if j != c -1:
            s.append(mat[i - 1][j + 1])
        s.append(mat[i - 1][j])
    if i != r -1:
        if j:
            s.append(mat[i + 1][j - 1])
        if j != c - 1:
            s.append(mat[i + 1][j + 1])
        s.append(mat[i + 1][j])
    if j:
        s.append(mat[i][j - 1])
    if j != c - 1:
        s.append(mat[i][j + 1])
    return s


if __name__ == '__main__':
    for i in annotate(["     ", "   * ", "     ", "     ", " *   "]):
        print(i)

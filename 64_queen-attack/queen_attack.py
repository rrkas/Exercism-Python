class Queen:
    def __init__(self, row, column):
        if (not (0 <= row <= 7)) or (not (0 <= column <= 7)):
            raise ValueError(' ')
        self.pos = (row, column)

    def can_attack(self, another_queen) -> bool:
        if self.pos == another_queen.pos:
            raise ValueError(' ')
        if self.pos[0] == another_queen.pos[0]:
            return True
        if self.pos[1] == another_queen.pos[1]:
            return True
        if abs(self.pos[0] - another_queen.pos[0]) == abs(self.pos[1] - another_queen.pos[1]):
            return True
        return False

# Globals for the directions
# Change the values as you see fit
EAST = 'e'
NORTH = 'n'
WEST = 'w'
SOUTH = 's'


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def move(self, instr):
        for m in instr:
            if self.direction==NORTH:
                if m == 'A':
                    self.coordinates = self.coordinates[0], self.coordinates[1] + 1
                elif m == 'R':
                    self.direction = EAST
                elif m == 'L':
                    self.direction = WEST
            elif self.direction == EAST:
                if m == 'A':
                    self.coordinates = self.coordinates[0] + 1, self.coordinates[1]
                elif m == 'R':
                    self.direction = SOUTH
                elif m == 'L':
                    self.direction = NORTH
            elif self.direction==SOUTH:
                if m == 'A':
                    self.coordinates = self.coordinates[0], self.coordinates[1] - 1
                elif m == 'R':
                    self.direction = WEST
                elif m == 'L':
                    self.direction = EAST
            elif self.direction == WEST:
                if m == 'A':
                    self.coordinates = self.coordinates[0] - 1, self.coordinates[1]
                elif m == 'R':
                    self.direction = NORTH
                elif m == 'L':
                    self.direction = SOUTH
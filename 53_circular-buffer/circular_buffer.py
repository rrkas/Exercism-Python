from collections import deque

class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.dq = deque()

    def read(self):
        try:
            return self.dq.popleft()
        except:
            raise BufferEmptyException(' ')

    def write(self, data):
        if len(self.dq) >= self.capacity:
            raise BufferFullException(' ')
        self.dq.append(data)

    def overwrite(self, data):
        if len(self.dq) >= self.capacity:
            self.dq.popleft()
        self.dq.append(data)

    def clear(self):
        self.dq.clear()


class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.start = 0
        self.end = 0

    def write(self, data):
        self.buffer[self.end] = data
        self.end = (self.end + 1) % self.size
        if self.end == self.start:
            self.start = (self.start + 1) % self.size

    def read(self):
        if self.start == self.end:
            return None
        data = self.buffer[self.start]
        self.start = (self.start + 1) % self.size
        return data

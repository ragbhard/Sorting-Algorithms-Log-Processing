
class MemoryPool:
    def __init__(self, block_size, pool_size):
        self.pool = [bytearray(block_size) for _ in range(pool_size)]
        self.free = list(range(pool_size))

    def allocate(self):
        if not self.free:
            raise MemoryError("Memory pool exhausted")
        return self.pool[self.free.pop()]

    def release(self, block):
        self.free.append(self.pool.index(block))

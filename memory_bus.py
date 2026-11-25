class MemoryBus:
    def __init__(self, memory, cache):
        self.memory = memory
        self.cache = cache

    def read(self, address): # return value from cache address, if cache miss, return value from memory address - return value
        if self.cache.contains(address):
            return self.cache.read(address)
        else:
            value = self.memory.read(address)
            self.cache.write(address, value)
            return value

    def write(self, address, value): # store value from cache address, if cache miss, return value from memory address
        self.cache.write(address, value)
        self.memory.write(address, value)

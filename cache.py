class Cache:
    def __init__(self, size = 8):
        self.size = size
        self.store = {} # {memory_address: value}

    def contains(self, address): # check if address in cache
        return address in self.store

    def read(self, address): # return value from cache address - return value
        return self.store[address]

    def write(self, address, value): # store value to cache address
        if len(self.store) == self.size:
            self.remove()
        else:
            self.store[address] = value

    def remove(self): # remove value from cache address if cache full FIFO
        self.store.popitem(last = False)
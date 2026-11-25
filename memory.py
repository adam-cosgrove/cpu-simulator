class Memory:
    def __init__(self, size):
        self.size = size
        self.data = [0] * self.size

    def read(self, address): # return value from memory address - return value
        if 0 <= address < self.size:
            return self.data[address]
        else:
            raise ValueError(f"Memory read out of bounds at address {address}")

    def write(self, address, value): # store value to memory address
        if 0 <= address < self.size:
            self.data[address] = value
        else:
            raise ValueError(f"Memory read out of bounds at address {address}")

    def load_data(self, path): # load values from file into memory address
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                address_binary, value_str  = line.split(",")

                address = int(address_binary, 2)

                value = int(value_str)

                self.write(address, value)


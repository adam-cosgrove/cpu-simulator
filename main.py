from memory import Memory
from cache import Cache
from memory_bus import MemoryBus
from cpu import CPU

def main():

    memory = Memory(size = 256)

    memory.load_data("data_input.txt")

    cache = Cache(size=4)

    memory_bus = MemoryBus(memory, cache)

    cpu = CPU(memory_bus)

    cpu.load_program("instruction_input.txt")

    cpu.run()

if __name__ == "__main__":
    main()
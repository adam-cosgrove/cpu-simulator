class CPU:
    def __init__(self, memory_bus):
        self.memory_bus = memory_bus
        self.running = True
        self.pc = 0
        self.registers = [0] * 8
        self.program = []

    def load_program(self, path):  # load instructions from file into program list
        with open(path, "r") as f:
            for line in f:
                self.program.append(line.strip())

    def fetch(self):  # retrieve instruction from program list
        instruction = self.program[self.pc]
        self.pc += 1
        return instruction

    def decode(self, instruction):  # decode instruction
        parts = instruction.split(",")
        opcode = parts[0].strip().upper()
        operands = [p.strip() for p in parts[1:]] if len(parts) > 1 else []
        return opcode, operands

    def execute(self, opcode, operands):  # execute opcode
        if opcode == "CACHE":
            self._exec_cache(operands)
        elif opcode == "LOAD":
            self._exec_load(operands)
        elif opcode == "LOADI":
            self._exec_loadi(operands)
        elif opcode == "STORE":
            self._exec_store(operands)
        elif opcode == "ADD":
            self._exec_add(operands)
        elif opcode == "ADDI":
            self._exec_addi(operands)
        elif opcode == "SUB":
            self._exec_sub(operands)
        elif opcode == "J":
            self._exec_jump(operands)
        elif opcode == "HALT":
            self.halt()
        else:
            raise ValueError(f"Unknown opcode {opcode}")

    # --- Helper functions for each opcode ---
    def _exec_cache(self, operands):
        addr = int(operands[0])
        value = self.memory_bus.read(addr)
        print(f"CACHE read at {addr}: {value}")

    def _exec_load(self, operands):
        reg = int(operands[0][1:])  # "R1" → 1
        addr = int(operands[1])
        self.registers[reg] = self.memory_bus.read(addr)

    def _exec_loadi(self, operands):
        reg = int(operands[0][1:])
        imm = int(operands[1])
        self.registers[reg] = imm

    def _exec_store(self, operands):
        reg = int(operands[0][1:])
        addr = int(operands[1])
        self.memory_bus.write(addr, self.registers[reg])

    def _exec_add(self, operands):
        reg1 = int(operands[0][1:])
        reg2 = int(operands[1][1:])
        self.registers[reg1] = self.alu(self.registers[reg1], self.registers[reg2], "ADD")

    def _exec_addi(self, operands):
        reg = int(operands[0][1:])
        imm = int(operands[1])
        self.registers[reg] = self.alu(self.registers[reg], imm, "ADD")

    def _exec_sub(self, operands):
        reg1 = int(operands[0][1:])
        reg2 = int(operands[1][1:])
        self.registers[reg1] = self.alu(self.registers[reg1], self.registers[reg2], "SUB")

    def _exec_jump(self, operands):
        addr = int(operands[0])
        self.pc = addr

    def alu(self, a, b, op):
        if op == "ADD":
            return a + b
        elif op == "SUB":
            return a - b

    def halt(self):
        self.running = False

    def run(self):  # main loop
        while self.running and self.pc < len(self.program):
            instr = self.fetch()
            opcode, operands = self.decode(instr)
            self.execute(opcode, operands)

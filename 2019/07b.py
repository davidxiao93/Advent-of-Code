from typing import List, Tuple
from collections import namedtuple

import file_loader

input_string = file_loader.get_input()
int_codes = [int(x) for x in input_string.split(",")]

Param = namedtuple("Param", ["mode", "value"])

opcodes = {
    1: (3, "add"),
    2: (3, "multiply"),
    3: (1, "read-input_string"),
    4: (1, "write-output"),
    5: (2, "jump-if-true"),
    6: (2, "jump-if-false"),
    7: (3, "less-than"),
    8: (3, "equals"),
    99: (0, "halt")
}

class Computer:
    def __init__(self, int_codes: List[int]):
        self.int_codes = int_codes.copy()
        self.current_instruction = 0
        self.inputs_queue = []
        self.outputs_queue = []
        self.halted = False

    def _parse_next_instruction(self) -> Tuple[str, List[Param]]:
        opcode = self.int_codes[self.current_instruction] % 100
        if opcode not in opcodes:
            print("unknown opcode")
            exit(1)
        params = []
        parameter_mode = self.int_codes[self.current_instruction] // 100
        for param_value in self.int_codes[self.current_instruction + 1:self.current_instruction + 1 + opcodes[opcode][0]]:
            param_mode = parameter_mode % 10
            params.append(Param(param_mode, param_value))
            parameter_mode = parameter_mode // 10
        return opcodes[opcode][1], params

    def _read_param(self, param: Param):
        if param.mode == 0:
            if param.value < 0:
                print("Warning, param value is negative! Continuing as though this isnt a problem")
            return self.int_codes[param.value]
        elif param.mode == 1:
            return param.value
        else:
            print("Unknown param mode")
            exit(1)

    def put_input(self, i):
        self.inputs_queue.append(i)

    def has_output(self):
        return len(self.outputs_queue) > 0

    def pop_next_output(self):
        if len(self.outputs_queue) > 0:
            return self.outputs_queue.pop(0)
        return None

    def run_step(self):
        if self.halted:
            return
        opcode, params = self._parse_next_instruction()
        jumped = False
        if opcode == "add":
            self.int_codes[params[2].value] = self._read_param(params[0]) + self._read_param(params[1])
        elif opcode == "multiply":
            self.int_codes[params[2].value] = self._read_param(params[0]) * self._read_param(params[1])
        elif opcode == "read-input_string":
            if len(self.inputs_queue) == 0:
                # Can't do anything now
                return
            self.int_codes[params[0].value] = self.inputs_queue.pop(0)
        elif opcode == "write-output":
            self.outputs_queue.append(self._read_param(params[0]))
        elif opcode == "jump-if-true":
            if self._read_param(params[0]) != 0:
                self.current_instruction = self._read_param(params[1])
                jumped = True
        elif opcode == "jump-if-false":
            if self._read_param(params[0]) == 0:
                self.current_instruction = self._read_param(params[1])
                jumped = True
        elif opcode == "less-than":
            self.int_codes[params[2].value] = 1 if self._read_param(params[0]) < self._read_param(params[1]) else 0
        elif opcode == "equals":
            self.int_codes[params[2].value] = 1 if self._read_param(params[0]) == self._read_param(params[1]) else 0
        elif opcode == "halt":
            self.halted = True
        else:
            print("unknown opcode")
            exit(1)
        if not jumped:
            self.current_instruction += 1 + len(params)


from itertools import permutations
most_thruster = 0
for perm in permutations(range(5, 10)):
    computers = [Computer(int_codes) for i in range(5)]
    for i, p in enumerate(perm):
        # set phase setting
        computers[i].put_input(p)
    # set first amp input_string signal
    last_output = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }
    current_computer = 0
    while True:
        c = computers[current_computer]
        prev_computer = (current_computer - 1) % 5
        c.put_input(last_output[prev_computer])
        while not c.has_output() and not c.halted:
            c.run_step()
        last_output[current_computer] = c.pop_next_output()
        if last_output[current_computer] is None:
            break
        current_computer = (current_computer + 1) % 5
    thruster = last_output[4]
    if thruster > most_thruster:
        most_thruster = thruster
print(most_thruster)















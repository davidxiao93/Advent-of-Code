from typing import List, Tuple
from collections import namedtuple

import file_loader

input_string = file_loader.get_input()

int_codes = [int(x) for x in input_string.split(",")]


Param = namedtuple("Param", ["mode", "value"])

opcodes = {
    1: (3, "add"),
    2: (3, "multiply"),
    3: (1, "read-input"),
    4: (1, "write-output"),
    5: (2, "jump-if-true"),
    6: (2, "jump-if-false"),
    7: (3, "less-than"),
    8: (3, "equals"),
    9: (1, "adjust-rel-base"),
    99: (0, "halt")
}

class Computer:
    def __init__(self, int_codes: List[int]):
        self.int_codes = {
            i: v
            for i, v in enumerate(int_codes)
        }
        self.current_instruction = 0
        self.inputs_queue = []
        self.outputs_queue = []
        self.halted = False
        self.waiting_for_input = False
        self.relative_base = 0

    def _parse_next_instruction(self) -> Tuple[str, List[Param]]:
        opcode = self.int_codes[self.current_instruction] % 100
        if opcode not in opcodes:
            print("unknown opcode")
            exit(1)
        params = []
        parameter_mode = self.int_codes[self.current_instruction] // 100
        param_values = [
            self.int_codes[x]
            for x in range(
                self.current_instruction + 1,
                self.current_instruction + 1 + opcodes[opcode][0]
            )
        ]
        for param_value in param_values:
            param_mode = parameter_mode % 10
            params.append(Param(param_mode, param_value))
            parameter_mode = parameter_mode // 10
        return opcodes[opcode][1], params

    def _read_param(self, param: Param):
        if param.mode == 0:
            key = param.value
        elif param.mode == 1:
            return param.value
        elif param.mode == 2:
            key = param.value + self.relative_base
        else:
            print("Unknown param mode for reading")
            exit(1)
            return # shut up the linter
        if key < 0:
            print("Cannot read from negative address")
            exit(1)
        if key not in self.int_codes:
            self.int_codes[key] = 0
        return self.int_codes[key]

    def _write_param(self, param: Param, value: int):
        if param.mode == 0:
            key = param.value
        elif param.mode == 1:
            print("Cannot write when param mode is 1")
            exit(1)
            return # shut up the linter
        elif param.mode == 2:
            key = param.value + self.relative_base
        else:
            print("Unknwon param mode for writing")
            exit(1)
            return # shut up the linter
        if key < 0:
            print("Cannot write to negative address")
            exit(1)
        self.int_codes[key] = value

    def put_input(self, i):
        self.inputs_queue.append(i)
        self.waiting_for_input = False

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
            self._write_param(params[2], self._read_param(params[0]) + self._read_param(params[1]))
        elif opcode == "multiply":
            self._write_param(params[2], self._read_param(params[0]) * self._read_param(params[1]))
        elif opcode == "read-input":
            if len(self.inputs_queue) == 0:
                # Can't do anything now
                self.waiting_for_input = True
                return
            self._write_param(params[0], self.inputs_queue.pop(0))
            self.waiting_for_input = False
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
            self._write_param(params[2], 1 if self._read_param(params[0]) < self._read_param(params[1]) else 0)
        elif opcode == "equals":
            self._write_param(params[2], 1 if self._read_param(params[0]) == self._read_param(params[1]) else 0)
        elif opcode == "halt":
            self.halted = True
        elif opcode == "adjust-rel-base":
            self.relative_base += self._read_param(params[0])
        else:
            print("unknown opcode")
            exit(1)
        if not jumped:
            self.current_instruction += 1 + len(params)



def run():
    commands = [
        "south",
        "east",
        "take asterisk",
        "west",
        "take monolith",
        "north",
        "west",
        "north",
        "east",
        #"take astronaut ice cream",
        "west",
        "south",
        #"take coin",
        "east",
        "north",
        "north",
        #"take mutex",
        "west",
        "take astrolabe",
        "west",
        #"take dehydrated water",
        "west",
        "take wreath",
        "east",
        "south",
        "east",
        "north",
        "north"
    ]
    output = ""
    c = Computer(int_codes)
    while True:
        while not c.halted and not c.has_output() and not c.waiting_for_input:
            c.run_step()
        if c.halted:
            print(output)
            return
        elif c.waiting_for_input:
            print(output)
            if len(commands) > 0:
                next_command = commands.pop(0)
            else:
                next_command = input_string()
            for s in next_command:
                c.put_input(ord(s))
            c.put_input(10) # newline
            output = ""
        else:
            while c.has_output():
                output += chr(c.pop_next_output())

run()



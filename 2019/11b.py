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
        self.blocked = False
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
        elif opcode == "read-input_string":
            if len(self.inputs_queue) == 0:
                # Can't do anything now
                self.blocked = True
                return
            self._write_param(params[0], self.inputs_queue.pop(0))
            self.blocked = False
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

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)

up = Point(0, -1)
right = Point(1, 0)
down = Point(0, 1)
left = Point(-1, 0)

current_direction = 0
directions = [up, right, down, left]

painted_hull = {}
current_position = Point(0,0)

c = Computer(int_codes)
while True:
    if current_position not in painted_hull:
        if current_position == Point(0,0):
            current_colour = 1
        else:
            current_colour = 0
    else:
        current_colour = painted_hull[current_position]
    while not c.has_output() and not c.halted:
        c.run_step()
        if c.blocked:
            c.put_input(current_colour)
    if c.halted:
        break
    new_colour = c.pop_next_output()
    painted_hull[current_position] = new_colour
    while not c.has_output() and not c.halted:
        c.run_step()
        if c.blocked:
            print("Help")
    if c.halted:
        break
    new_dir = c.pop_next_output()
    if new_dir == 1:
        current_direction = (current_direction + 1) % 4
    else:
        current_direction = (current_direction - 1) % 4
    current_position = add_point(current_position, directions[current_direction])

# print(len(painted_hull))

min_x = min(painted_hull.keys(), key = lambda p: p.x).x
min_y = min(painted_hull.keys(), key = lambda p: p.y).y
max_x = max(painted_hull.keys(), key = lambda p: p.x).x
max_y = max(painted_hull.keys(), key = lambda p: p.y).y

for y in range(min_y - 1, max_y + 2):
    row = []
    for x in range(min_x - 1, max_x + 2):
        p = Point(x, y)
        if p in painted_hull:
            colour = painted_hull[p]
        else:
            colour = 0
        row.append("#" if colour == 1 else " ")
    print("".join(row))


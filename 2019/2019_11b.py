from typing import List, Tuple
from collections import namedtuple

input = """3,8,1005,8,299,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,29,1,1007,14,10,2,1106,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,58,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,80,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,103,1,5,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,128,1,106,18,10,1,7,20,10,1006,0,72,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,164,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,186,1,1007,8,10,1006,0,98,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,216,2,102,8,10,1,1008,18,10,1,1108,8,10,1006,0,68,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,253,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,274,1,1105,7,10,101,1,9,9,1007,9,1060,10,1005,10,15,99,109,621,104,0,104,1,21102,936995738520,1,1,21102,316,1,0,1106,0,420,21101,0,936995824276,1,21102,1,327,0,1106,0,420,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,248129784923,1,1,21102,1,374,0,1105,1,420,21102,29015149735,1,1,21101,385,0,0,1106,0,420,3,10,104,0,104,0,3,10,104,0,104,0,21101,983925826304,0,1,21101,0,408,0,1105,1,420,21102,825012036364,1,1,21101,0,419,0,1105,1,420,99,109,2,22101,0,-1,1,21101,0,40,2,21101,0,451,3,21102,441,1,0,1105,1,484,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,446,447,462,4,0,1001,446,1,446,108,4,446,10,1006,10,478,1101,0,0,446,109,-2,2105,1,0,0,109,4,2102,1,-1,483,1207,-3,0,10,1006,10,501,21102,0,1,-3,21201,-3,0,1,22102,1,-2,2,21102,1,1,3,21101,520,0,0,1106,0,525,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,548,2207,-4,-2,10,1006,10,548,21201,-4,0,-4,1105,1,616,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,567,0,1105,1,525,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,586,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,608,21201,-1,0,1,21102,1,608,0,106,0,483,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"""
int_codes = [int(x) for x in input.split(",")]

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
        elif opcode == "read-input":
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

print(len(painted_hull))

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


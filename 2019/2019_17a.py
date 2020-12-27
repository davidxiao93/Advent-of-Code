from typing import List, Tuple
from collections import namedtuple

input = """1,330,331,332,109,2650,1102,1,1182,15,1102,1429,1,24,1001,0,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,15,1,15,1008,15,1429,570,1006,570,14,21102,58,1,0,1105,1,786,1006,332,62,99,21101,333,0,1,21102,1,73,0,1105,1,579,1102,0,1,572,1102,1,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,1002,574,1,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1106,0,81,21101,0,340,1,1105,1,177,21101,477,0,1,1105,1,177,21102,1,514,1,21101,0,176,0,1105,1,579,99,21101,184,0,0,1105,1,579,4,574,104,10,99,1007,573,22,570,1006,570,165,1002,572,1,1182,21102,1,375,1,21102,1,211,0,1105,1,579,21101,1182,11,1,21101,0,222,0,1106,0,979,21101,388,0,1,21102,233,1,0,1106,0,579,21101,1182,22,1,21102,244,1,0,1105,1,979,21102,1,401,1,21101,255,0,0,1105,1,579,21101,1182,33,1,21102,266,1,0,1105,1,979,21102,414,1,1,21102,277,1,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21101,0,313,0,1106,0,622,1005,575,327,1102,1,1,575,21102,1,327,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,36,16,0,109,4,2102,1,-3,587,20102,1,0,-1,22101,1,-3,-3,21102,0,1,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2105,1,0,109,5,2102,1,-4,630,20101,0,0,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20102,1,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,0,702,0,1106,0,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21101,731,0,0,1105,1,786,1106,0,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1106,0,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21102,1,774,0,1105,1,622,21201,-3,1,-3,1105,1,640,109,-5,2106,0,0,109,7,1005,575,802,20101,0,576,-6,20101,0,577,-5,1106,0,814,21102,0,1,-1,21101,0,0,-5,21101,0,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,37,-3,22201,-6,-3,-3,22101,1429,-3,-3,1202,-3,1,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21101,0,1,-1,1106,0,924,1205,-2,873,21101,35,0,-4,1105,1,924,2102,1,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2102,1,-3,895,1102,1,2,0,2102,1,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,921,21001,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,37,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,33,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,973,1,0,1106,0,786,99,109,-7,2106,0,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1105,1,1041,21101,0,-4,-2,1105,1,1041,21102,-5,1,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1201,-2,0,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,2101,0,-2,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21101,0,439,1,1105,1,1150,21101,0,477,1,1105,1,1150,21101,0,514,1,21102,1,1149,0,1106,0,579,99,21101,1157,0,0,1106,0,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,1202,-5,1,1176,2102,1,-4,0,109,-6,2105,1,0,8,7,30,1,5,1,30,1,5,1,30,1,5,1,22,9,1,9,18,1,9,1,3,1,3,1,18,1,3,11,3,1,18,1,3,1,5,1,7,1,18,1,3,1,5,1,7,1,1,5,1,7,4,1,3,1,5,1,7,1,1,1,3,1,1,1,5,1,4,11,7,1,1,1,3,1,1,1,5,1,8,1,13,1,1,1,3,1,1,1,5,1,8,1,13,1,1,11,1,1,8,1,13,1,5,1,1,1,5,1,8,7,7,7,1,1,5,1,14,1,15,1,5,1,14,1,15,1,5,5,10,1,15,1,20,1,1,7,7,7,14,1,1,1,5,1,13,1,10,11,1,1,13,1,10,1,3,1,1,1,3,1,1,1,13,1,10,1,3,1,1,1,3,1,1,1,7,11,6,1,3,1,1,1,3,1,1,1,7,1,5,1,3,1,6,5,1,5,1,1,7,1,5,1,3,1,18,1,7,1,5,1,3,1,18,1,3,11,3,1,18,1,3,1,3,1,9,1,18,9,1,9,22,1,5,1,30,1,5,1,30,1,5,1,30,7,8"""
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

c = Computer(int_codes)

outputs = []
while not c.halted and not c.waiting_for_input:
    while not c.halted and not c.waiting_for_input and not c.has_output():
        c.run_step()
    while c.has_output():
        outputs.append(c.pop_next_output())

image = "".join([chr(c) for c in outputs])


Point = namedtuple("Point", ["x", "y"])
up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)
directions = [up, right, down, left]

def add_point(p: Point, q: Point):
    return Point(p.x + q.x, p.y + q.y)

scaffolding = set()
current_pos = None
current_direction = None
for y, line in enumerate(image.splitlines()):
    for x, p in enumerate(line):
        if p != ".":
            scaffolding.add(Point(x, y))
            if p != "#":
                current_pos = Point(x, y)
                if p == "^":
                    current_direction = 0
                elif p == ">":
                    current_direction = 1
                elif p == "v":
                    current_direction = 2
                elif p == "<":
                    current_direction = 3

assert(current_pos is not None)
assert(current_direction is not None)

intersections = set()
for s in scaffolding:
    surrounded = True
    for d in directions:
        if add_point(s, d) not in scaffolding:
            surrounded = False
            break
    if surrounded:
        intersections.add(s)

print(sum([
    x*y for x, y in intersections
]))

from typing import List, Tuple
from collections import namedtuple

input = """1,380,379,385,1008,2399,203850,381,1005,381,12,99,109,2400,1101,0,0,383,1102,1,0,382,20101,0,382,1,21001,383,0,2,21101,37,0,0,1105,1,578,4,382,4,383,204,1,1001,382,1,382,1007,382,44,381,1005,381,22,1001,383,1,383,1007,383,20,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1105,1,161,107,1,392,381,1006,381,161,1102,1,-1,384,1105,1,119,1007,392,42,381,1006,381,161,1102,1,1,384,20101,0,392,1,21101,18,0,2,21102,1,0,3,21101,138,0,0,1105,1,549,1,392,384,392,21001,392,0,1,21101,18,0,2,21102,1,3,3,21102,161,1,0,1105,1,549,1101,0,0,384,20001,388,390,1,21001,389,0,2,21102,1,180,0,1106,0,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,20101,0,389,2,21102,205,1,0,1105,1,393,1002,390,-1,390,1101,0,1,384,21002,388,1,1,20001,389,391,2,21101,0,228,0,1105,1,578,1206,1,261,1208,1,2,381,1006,381,253,21001,388,0,1,20001,389,391,2,21102,1,253,0,1106,0,393,1002,391,-1,391,1101,0,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21102,279,1,0,1105,1,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21102,1,304,0,1106,0,393,1002,390,-1,390,1002,391,-1,391,1102,1,1,384,1005,384,161,20101,0,388,1,21002,389,1,2,21101,0,0,3,21101,338,0,0,1106,0,549,1,388,390,388,1,389,391,389,21001,388,0,1,20101,0,389,2,21102,4,1,3,21101,0,365,0,1106,0,549,1007,389,19,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,341,20,15,1,1,22,109,3,22101,0,-2,1,22102,1,-1,2,21101,0,0,3,21102,1,414,0,1105,1,549,22102,1,-2,1,22102,1,-1,2,21102,429,1,0,1106,0,601,1202,1,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,21202,-3,1,-7,109,-8,2105,1,0,109,4,1202,-2,44,566,201,-3,566,566,101,639,566,566,1201,-1,0,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,44,594,201,-2,594,594,101,639,594,594,20101,0,0,-2,109,-3,2106,0,0,109,3,22102,20,-2,1,22201,1,-1,1,21101,0,443,2,21102,1,526,3,21102,880,1,4,21102,1,630,0,1105,1,456,21201,1,1519,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,2,2,2,0,0,2,2,0,2,0,0,2,2,2,2,0,2,2,2,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,0,2,0,1,1,0,2,0,0,2,0,2,2,2,0,2,0,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,2,0,2,0,0,0,2,2,0,0,2,2,2,2,0,1,1,0,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,0,2,2,2,2,0,0,0,2,2,0,2,2,2,2,2,2,0,0,2,2,2,2,2,2,0,1,1,0,2,0,2,2,2,2,2,0,0,2,0,0,2,0,2,2,2,2,2,2,2,0,2,0,0,2,0,2,2,2,0,2,2,2,2,2,2,2,2,2,0,1,1,0,2,2,2,0,2,0,0,2,2,0,2,2,2,0,2,0,2,2,2,2,2,0,0,0,2,0,0,2,2,2,0,2,2,0,0,0,2,2,2,0,0,1,1,0,2,2,2,2,2,2,2,0,0,2,2,2,2,0,0,2,2,2,0,2,2,2,0,2,2,2,2,0,2,0,2,2,0,2,2,2,0,2,0,2,0,1,1,0,2,2,2,2,0,2,0,2,2,2,2,2,2,2,2,0,0,0,2,2,2,0,2,0,2,0,2,2,2,2,0,2,2,0,2,0,2,0,2,0,0,1,1,0,2,2,2,2,0,2,2,0,2,2,0,0,0,2,0,2,2,2,2,0,2,0,0,0,2,2,0,2,2,2,2,0,0,2,2,2,2,0,2,2,0,1,1,0,2,2,2,0,2,2,0,2,2,2,2,2,2,2,2,2,2,2,0,2,0,0,2,2,2,2,0,2,2,2,0,2,2,2,2,2,2,0,2,2,0,1,1,0,2,2,2,2,2,0,2,2,2,0,2,2,0,0,2,2,2,0,2,2,2,2,2,2,0,2,0,2,2,0,0,2,2,0,2,2,2,0,2,2,0,1,1,0,2,2,2,2,2,0,2,2,2,0,2,2,2,2,2,0,2,0,2,2,2,0,2,0,0,2,0,2,2,2,2,2,2,2,0,2,2,2,2,2,0,1,1,0,0,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,2,0,2,2,2,2,2,2,2,2,0,2,0,0,2,2,0,2,0,2,2,2,2,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,11,38,49,70,10,39,91,58,63,68,52,75,23,63,39,47,35,75,29,29,52,19,47,94,19,66,22,88,37,37,78,74,50,60,79,90,76,65,62,46,70,10,5,78,40,26,89,43,42,11,26,57,77,13,3,28,60,91,71,34,83,69,11,40,97,12,59,2,35,50,62,24,93,66,1,29,31,31,70,97,37,72,39,55,83,60,6,81,2,6,49,73,44,59,88,14,13,76,25,30,85,82,12,12,20,34,11,87,11,95,16,28,84,79,10,96,48,55,62,38,1,7,65,7,63,5,30,52,48,77,31,39,87,20,70,4,91,56,48,20,90,21,89,90,27,37,20,72,89,82,93,84,30,53,85,86,16,7,1,14,2,61,75,25,57,53,89,8,36,29,22,66,21,97,55,19,65,29,55,98,40,48,84,32,87,53,98,98,63,14,29,42,63,90,30,53,58,45,31,2,16,78,84,26,86,59,68,70,42,2,45,90,62,32,62,9,68,14,27,89,97,11,96,60,6,43,29,56,2,80,52,76,92,44,66,62,13,95,7,84,81,47,7,69,33,35,33,65,7,83,15,92,49,18,31,91,40,96,44,64,56,77,31,6,16,68,13,77,32,76,29,23,92,75,32,86,45,94,88,26,79,17,29,70,14,91,9,9,71,79,1,25,72,5,16,62,3,92,8,58,30,9,11,21,7,13,26,11,65,17,83,43,94,78,10,72,96,53,53,61,53,31,73,36,12,66,65,88,81,97,54,82,60,18,81,77,46,31,68,67,55,85,63,42,43,44,71,37,31,94,63,41,61,26,9,16,78,85,54,8,62,86,91,58,42,14,85,25,62,75,55,60,1,94,84,49,67,70,96,16,97,40,5,80,83,58,24,7,42,27,33,97,97,95,94,8,44,18,64,96,80,80,14,16,27,43,26,52,32,41,6,44,83,53,89,11,50,43,64,46,9,97,21,38,59,70,89,18,98,17,69,95,44,70,35,73,22,94,4,78,11,74,15,72,87,84,85,75,34,17,65,11,96,86,39,69,55,59,56,58,97,39,54,70,71,25,15,97,29,66,78,54,54,82,92,28,28,60,98,8,18,5,30,4,3,15,65,4,89,76,27,90,36,47,75,70,82,95,44,13,63,56,36,43,92,66,61,85,73,71,60,51,56,90,44,40,73,15,76,67,51,36,44,12,58,45,17,80,97,30,57,47,96,3,95,2,27,77,84,13,69,89,78,8,45,58,22,74,84,12,10,32,16,20,4,21,98,52,55,77,24,14,38,76,82,73,39,5,19,51,75,89,31,51,60,95,89,2,15,39,17,17,77,79,60,21,21,87,81,1,95,5,5,59,3,93,3,34,51,56,11,39,29,34,56,65,36,20,16,44,28,11,44,15,59,95,30,24,33,24,64,4,6,96,62,72,40,93,30,42,45,81,49,82,77,58,9,18,60,86,53,90,57,69,26,86,67,97,90,79,77,64,19,27,13,10,89,92,33,1,23,97,72,19,11,25,89,87,65,54,93,78,34,49,36,82,61,59,76,9,97,39,32,26,54,62,62,3,33,75,29,87,6,30,92,14,23,33,58,95,92,52,12,95,70,18,64,11,81,76,47,85,40,52,51,65,91,18,30,63,59,63,66,39,76,87,63,98,65,67,17,72,63,9,73,74,12,79,35,48,17,68,40,50,13,46,75,61,53,50,26,37,44,92,46,6,42,17,85,56,85,75,90,63,73,61,74,5,18,70,39,75,67,6,16,10,36,80,28,69,37,42,39,19,40,9,4,49,8,97,82,2,44,86,86,95,49,40,26,86,71,45,11,61,9,98,82,67,88,47,54,86,89,97,6,31,59,9,81,24,76,59,95,19,40,63,9,90,83,10,45,96,80,57,16,8,97,64,36,28,37,88,64,47,19,51,92,30,15,55,2,7,73,22,2,8,82,69,39,63,48,43,27,23,40,82,57,19,42,36,92,57,66,54,8,48,94,76,70,76,203850"""
int_codes = [int(x) for x in input.split(",")]

# add quarter
int_codes[0] = 2

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


next_input = 0
paddle = None
ball = None
score = None
blocks = set()

iterate_once = True

while len(blocks) != 0 or iterate_once:
    iterate_once = False
    outputs = []
    c.put_input(next_input)
    while not c.halted and not c.waiting_for_input:
        while not c.halted and not c.has_output() and not c.waiting_for_input:
            c.run_step()
        if c.has_output():
            outputs.append(c.pop_next_output())

    for i in range(len(outputs))[2::3]:
        x = outputs[i-2]
        y = outputs[i-1]
        tile_id = outputs[i]
        if tile_id == 3: # paddle
            paddle = (x, y)
        elif tile_id == 4: # ball
            ball = (x, y)
        elif x == -1 and y == 0:
            score = tile_id
        elif tile_id == 2:
            blocks.add((x, y))
        elif tile_id == 0 and (x, y) in blocks:
            # block has been removed
            blocks.remove((x, y))

    # Move paddle to follow ball
    if paddle[0] < ball[0]:
        next_input = 1
    elif paddle[0] == ball[0]:
        next_input = 0
    else:
        next_input = -1

print(score)

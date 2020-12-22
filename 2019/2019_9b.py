from typing import List, Tuple
from collections import namedtuple

input = """1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,1,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,26,1,1005,1101,0,24,1019,1102,1,32,1007,1101,0,704,1027,1102,0,1,1020,1101,0,348,1029,1102,28,1,1002,1101,34,0,1016,1102,29,1,1008,1102,1,30,1013,1102,25,1,1012,1101,0,33,1009,1102,1,37,1001,1101,31,0,1017,1101,245,0,1022,1102,39,1,1000,1101,27,0,1011,1102,770,1,1025,1101,0,22,1015,1102,1,1,1021,1101,711,0,1026,1101,20,0,1004,1101,0,23,1018,1101,242,0,1023,1102,21,1,1003,1101,38,0,1010,1101,0,35,1014,1101,0,36,1006,1101,0,357,1028,1102,1,775,1024,109,-3,2102,1,9,63,1008,63,36,63,1005,63,203,4,187,1105,1,207,1001,64,1,64,1002,64,2,64,109,8,21101,40,0,5,1008,1010,41,63,1005,63,227,1106,0,233,4,213,1001,64,1,64,1002,64,2,64,109,16,2105,1,2,1105,1,251,4,239,1001,64,1,64,1002,64,2,64,109,1,21107,41,40,-4,1005,1018,271,1001,64,1,64,1105,1,273,4,257,1002,64,2,64,109,-18,1207,0,21,63,1005,63,295,4,279,1001,64,1,64,1105,1,295,1002,64,2,64,109,-3,1207,0,36,63,1005,63,311,1105,1,317,4,301,1001,64,1,64,1002,64,2,64,109,6,2108,20,-3,63,1005,63,339,4,323,1001,64,1,64,1106,0,339,1002,64,2,64,109,28,2106,0,-7,4,345,1001,64,1,64,1106,0,357,1002,64,2,64,109,-18,1206,4,373,1001,64,1,64,1105,1,375,4,363,1002,64,2,64,109,-6,2107,31,-4,63,1005,63,397,4,381,1001,64,1,64,1105,1,397,1002,64,2,64,109,1,21102,42,1,-1,1008,1011,39,63,1005,63,421,1001,64,1,64,1106,0,423,4,403,1002,64,2,64,109,-2,2108,26,-2,63,1005,63,439,1106,0,445,4,429,1001,64,1,64,1002,64,2,64,109,6,21102,43,1,-5,1008,1011,43,63,1005,63,467,4,451,1105,1,471,1001,64,1,64,1002,64,2,64,109,6,21101,44,0,-3,1008,1019,44,63,1005,63,493,4,477,1105,1,497,1001,64,1,64,1002,64,2,64,109,-9,1206,7,511,4,503,1105,1,515,1001,64,1,64,1002,64,2,64,109,14,1205,-7,531,1001,64,1,64,1106,0,533,4,521,1002,64,2,64,109,-27,1201,0,0,63,1008,63,39,63,1005,63,555,4,539,1105,1,559,1001,64,1,64,1002,64,2,64,109,10,2101,0,-5,63,1008,63,24,63,1005,63,583,1001,64,1,64,1105,1,585,4,565,1002,64,2,64,109,-11,2107,21,5,63,1005,63,601,1105,1,607,4,591,1001,64,1,64,1002,64,2,64,109,10,1208,0,36,63,1005,63,627,1001,64,1,64,1106,0,629,4,613,1002,64,2,64,109,15,21108,45,45,-9,1005,1015,647,4,635,1105,1,651,1001,64,1,64,1002,64,2,64,109,-19,2101,0,-4,63,1008,63,37,63,1005,63,677,4,657,1001,64,1,64,1106,0,677,1002,64,2,64,109,22,1205,-6,695,4,683,1001,64,1,64,1105,1,695,1002,64,2,64,109,-10,2106,0,10,1001,64,1,64,1105,1,713,4,701,1002,64,2,64,109,-9,1201,-8,0,63,1008,63,36,63,1005,63,733,1105,1,739,4,719,1001,64,1,64,1002,64,2,64,109,7,21107,46,47,0,1005,1015,757,4,745,1106,0,761,1001,64,1,64,1002,64,2,64,109,14,2105,1,-5,4,767,1105,1,779,1001,64,1,64,1002,64,2,64,109,-34,2102,1,6,63,1008,63,39,63,1005,63,799,1105,1,805,4,785,1001,64,1,64,1002,64,2,64,109,25,21108,47,49,-4,1005,1016,825,1001,64,1,64,1106,0,827,4,811,1002,64,2,64,109,-6,1208,-8,36,63,1005,63,845,4,833,1106,0,849,1001,64,1,64,1002,64,2,64,109,-10,1202,2,1,63,1008,63,36,63,1005,63,875,4,855,1001,64,1,64,1105,1,875,1002,64,2,64,109,-5,1202,10,1,63,1008,63,30,63,1005,63,895,1106,0,901,4,881,1001,64,1,64,4,64,99,21101,27,0,1,21101,0,915,0,1105,1,922,21201,1,65916,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1105,1,922,21201,1,0,-1,21201,-2,-3,1,21102,1,957,0,1105,1,922,22201,1,-1,-2,1106,0,968,22102,1,-2,-2,109,-3,2105,1,0"""
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
                return
            self._write_param(params[0], self.inputs_queue.pop(0))
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
c.put_input(2)
while not c.halted:
    c.run_step()
    if c.has_output():
        print(c.pop_next_output())


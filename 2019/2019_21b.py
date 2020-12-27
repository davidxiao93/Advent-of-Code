from typing import List, Tuple
from collections import namedtuple

input = """109,2050,21101,0,966,1,21102,13,1,0,1105,1,1378,21101,0,20,0,1106,0,1337,21102,27,1,0,1106,0,1279,1208,1,65,748,1005,748,73,1208,1,79,748,1005,748,110,1208,1,78,748,1005,748,132,1208,1,87,748,1005,748,169,1208,1,82,748,1005,748,239,21102,1,1041,1,21102,1,73,0,1106,0,1421,21102,1,78,1,21102,1,1041,2,21101,0,88,0,1105,1,1301,21101,68,0,1,21102,1041,1,2,21102,103,1,0,1105,1,1301,1101,1,0,750,1106,0,298,21101,82,0,1,21101,0,1041,2,21102,1,125,0,1106,0,1301,1102,2,1,750,1105,1,298,21102,1,79,1,21101,1041,0,2,21101,147,0,0,1106,0,1301,21102,84,1,1,21101,1041,0,2,21101,162,0,0,1105,1,1301,1101,3,0,750,1105,1,298,21102,1,65,1,21101,0,1041,2,21102,184,1,0,1106,0,1301,21102,1,76,1,21102,1,1041,2,21102,1,199,0,1106,0,1301,21102,75,1,1,21102,1041,1,2,21101,214,0,0,1106,0,1301,21101,221,0,0,1105,1,1337,21102,10,1,1,21102,1,1041,2,21102,236,1,0,1105,1,1301,1106,0,553,21102,1,85,1,21102,1041,1,2,21101,0,254,0,1106,0,1301,21101,78,0,1,21102,1,1041,2,21101,269,0,0,1105,1,1301,21102,1,276,0,1106,0,1337,21102,10,1,1,21102,1,1041,2,21101,0,291,0,1105,1,1301,1102,1,1,755,1105,1,553,21102,1,32,1,21102,1,1041,2,21101,313,0,0,1105,1,1301,21102,1,320,0,1106,0,1337,21101,327,0,0,1105,1,1279,2101,0,1,749,21102,1,65,2,21102,73,1,3,21101,0,346,0,1105,1,1889,1206,1,367,1007,749,69,748,1005,748,360,1102,1,1,756,1001,749,-64,751,1106,0,406,1008,749,74,748,1006,748,381,1101,-1,0,751,1105,1,406,1008,749,84,748,1006,748,395,1101,0,-2,751,1105,1,406,21101,0,1100,1,21101,406,0,0,1105,1,1421,21102,32,1,1,21102,1100,1,2,21102,421,1,0,1105,1,1301,21101,428,0,0,1106,0,1337,21101,435,0,0,1105,1,1279,2102,1,1,749,1008,749,74,748,1006,748,453,1101,0,-1,752,1106,0,478,1008,749,84,748,1006,748,467,1102,-2,1,752,1106,0,478,21101,1168,0,1,21102,1,478,0,1106,0,1421,21102,1,485,0,1106,0,1337,21101,10,0,1,21102,1,1168,2,21101,0,500,0,1105,1,1301,1007,920,15,748,1005,748,518,21101,1209,0,1,21101,518,0,0,1105,1,1421,1002,920,3,529,1001,529,921,529,102,1,750,0,1001,529,1,537,1001,751,0,0,1001,537,1,545,1002,752,1,0,1001,920,1,920,1105,1,13,1005,755,577,1006,756,570,21101,1100,0,1,21102,570,1,0,1105,1,1421,21102,1,987,1,1105,1,581,21102,1001,1,1,21101,588,0,0,1105,1,1378,1102,758,1,594,102,1,0,753,1006,753,654,21002,753,1,1,21102,1,610,0,1106,0,667,21102,0,1,1,21102,621,1,0,1106,0,1463,1205,1,647,21101,1015,0,1,21102,635,1,0,1106,0,1378,21102,1,1,1,21101,0,646,0,1105,1,1463,99,1001,594,1,594,1106,0,592,1006,755,664,1101,0,0,755,1105,1,647,4,754,99,109,2,1102,726,1,757,22101,0,-1,1,21102,9,1,2,21101,697,0,3,21101,0,692,0,1105,1,1913,109,-2,2105,1,0,109,2,1001,757,0,706,2101,0,-1,0,1001,757,1,757,109,-2,2105,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,255,63,223,191,95,127,159,0,228,49,34,55,222,59,252,85,109,103,221,76,141,197,124,142,115,217,206,69,187,232,114,60,122,53,87,169,42,166,241,177,167,203,186,136,220,181,234,54,68,184,219,102,43,168,47,79,179,157,251,93,123,245,253,202,178,50,57,171,238,196,116,46,152,172,201,200,61,111,120,86,58,158,199,101,107,218,92,138,173,212,156,139,243,125,205,182,231,239,163,188,236,227,230,51,183,247,143,229,84,244,175,248,154,78,121,100,185,119,98,170,213,38,207,237,106,155,226,216,153,94,242,71,70,204,99,56,214,39,189,137,62,162,190,118,35,113,77,246,174,249,215,254,235,233,108,110,117,198,250,126,140,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,73,110,112,117,116,32,105,110,115,116,114,117,99,116,105,111,110,115,58,10,13,10,87,97,108,107,105,110,103,46,46,46,10,10,13,10,82,117,110,110,105,110,103,46,46,46,10,10,25,10,68,105,100,110,39,116,32,109,97,107,101,32,105,116,32,97,99,114,111,115,115,58,10,10,58,73,110,118,97,108,105,100,32,111,112,101,114,97,116,105,111,110,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,78,68,44,32,79,82,44,32,111,114,32,78,79,84,67,73,110,118,97,108,105,100,32,102,105,114,115,116,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,44,32,66,44,32,67,44,32,68,44,32,74,44,32,111,114,32,84,40,73,110,118,97,108,105,100,32,115,101,99,111,110,100,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,74,32,111,114,32,84,52,79,117,116,32,111,102,32,109,101,109,111,114,121,59,32,97,116,32,109,111,115,116,32,49,53,32,105,110,115,116,114,117,99,116,105,111,110,115,32,99,97,110,32,98,101,32,115,116,111,114,101,100,0,109,1,1005,1262,1270,3,1262,21001,1262,0,0,109,-1,2106,0,0,109,1,21102,1,1288,0,1106,0,1263,20102,1,1262,0,1102,0,1,1262,109,-1,2106,0,0,109,5,21102,1310,1,0,1106,0,1279,21201,1,0,-2,22208,-2,-4,-1,1205,-1,1332,22101,0,-3,1,21102,1,1332,0,1105,1,1421,109,-5,2106,0,0,109,2,21102,1,1346,0,1105,1,1263,21208,1,32,-1,1205,-1,1363,21208,1,9,-1,1205,-1,1363,1106,0,1373,21102,1,1370,0,1106,0,1279,1105,1,1339,109,-2,2105,1,0,109,5,2102,1,-4,1385,21001,0,0,-2,22101,1,-4,-4,21102,0,1,-3,22208,-3,-2,-1,1205,-1,1416,2201,-4,-3,1408,4,0,21201,-3,1,-3,1106,0,1396,109,-5,2106,0,0,109,2,104,10,22101,0,-1,1,21102,1,1436,0,1105,1,1378,104,10,99,109,-2,2106,0,0,109,3,20002,594,753,-1,22202,-1,-2,-1,201,-1,754,754,109,-3,2106,0,0,109,10,21101,5,0,-5,21102,1,1,-4,21101,0,0,-3,1206,-9,1555,21102,1,3,-6,21102,1,5,-7,22208,-7,-5,-8,1206,-8,1507,22208,-6,-4,-8,1206,-8,1507,104,64,1106,0,1529,1205,-6,1527,1201,-7,716,1515,21002,0,-11,-8,21201,-8,46,-8,204,-8,1106,0,1529,104,46,21201,-7,1,-7,21207,-7,22,-8,1205,-8,1488,104,10,21201,-6,-1,-6,21207,-6,0,-8,1206,-8,1484,104,10,21207,-4,1,-8,1206,-8,1569,21102,1,0,-9,1105,1,1689,21208,-5,21,-8,1206,-8,1583,21102,1,1,-9,1106,0,1689,1201,-5,716,1589,20101,0,0,-2,21208,-4,1,-1,22202,-2,-1,-1,1205,-2,1613,22102,1,-5,1,21102,1,1613,0,1106,0,1444,1206,-1,1634,21201,-5,0,1,21102,1,1627,0,1106,0,1694,1206,1,1634,21101,0,2,-3,22107,1,-4,-8,22201,-1,-8,-8,1206,-8,1649,21201,-5,1,-5,1206,-3,1663,21201,-3,-1,-3,21201,-4,1,-4,1106,0,1667,21201,-4,-1,-4,21208,-4,0,-1,1201,-5,716,1676,22002,0,-1,-1,1206,-1,1686,21101,1,0,-4,1105,1,1477,109,-10,2106,0,0,109,11,21101,0,0,-6,21101,0,0,-8,21102,0,1,-7,20208,-6,920,-9,1205,-9,1880,21202,-6,3,-9,1201,-9,921,1725,20101,0,0,-5,1001,1725,1,1732,21001,0,0,-4,21201,-4,0,1,21101,0,1,2,21101,0,9,3,21101,1754,0,0,1106,0,1889,1206,1,1772,2201,-10,-4,1766,1001,1766,716,1766,21002,0,1,-3,1106,0,1790,21208,-4,-1,-9,1206,-9,1786,22102,1,-8,-3,1105,1,1790,21202,-7,1,-3,1001,1732,1,1796,20101,0,0,-2,21208,-2,-1,-9,1206,-9,1812,22101,0,-8,-1,1106,0,1816,21201,-7,0,-1,21208,-5,1,-9,1205,-9,1837,21208,-5,2,-9,1205,-9,1844,21208,-3,0,-1,1106,0,1855,22202,-3,-1,-1,1106,0,1855,22201,-3,-1,-1,22107,0,-1,-1,1106,0,1855,21208,-2,-1,-9,1206,-9,1869,21202,-1,1,-8,1105,1,1873,21201,-1,0,-7,21201,-6,1,-6,1106,0,1708,22102,1,-8,-10,109,-11,2105,1,0,109,7,22207,-6,-5,-3,22207,-4,-6,-2,22201,-3,-2,-1,21208,-1,0,-6,109,-7,2106,0,0,0,109,5,1201,-2,0,1912,21207,-4,0,-1,1206,-1,1930,21101,0,0,-4,22102,1,-4,1,22101,0,-3,2,21101,0,1,3,21102,1949,1,0,1105,1,1954,109,-5,2106,0,0,109,6,21207,-4,1,-1,1206,-1,1977,22207,-5,-3,-1,1206,-1,1977,22101,0,-5,-5,1106,0,2045,22101,0,-5,1,21201,-4,-1,2,21202,-3,2,3,21102,1,1996,0,1105,1,1954,22102,1,1,-5,21102,1,1,-2,22207,-5,-3,-1,1206,-1,2015,21101,0,0,-2,22202,-3,-2,-3,22107,0,-4,-1,1206,-1,2037,22102,1,-2,1,21101,2037,0,0,106,0,1912,21202,-3,-1,-3,22201,-5,-3,-5,109,-6,2106,0,0"""
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

"""
must handle
     ABCDEFGHI
#####.###########
#####.##.########
#####...#########
#####.#.#..##.###
#####...##...####
#####...####..###
#####.#.##...####

if (!A or !B or !C) and D and ((!E and H) or E) then jump
!E and H -> does it need to jump immediately after landing on D
otherwise make sure it can move onto E
"""


springdroid_program = """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT E T
AND H T
OR E T
AND T J
RUN
"""

for s in springdroid_program:
    c.put_input(ord(s))
while not c.halted and not c.waiting_for_input:
    c.run_step()
while c.has_output():
    v = c.pop_next_output()
    if v > 128:
        print(v)

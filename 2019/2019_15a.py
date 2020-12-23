from typing import List, Tuple
from collections import namedtuple

input = """3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,1002,1036,1,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1106,0,124,1001,1034,0,1039,1002,1036,1,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,1001,1035,0,1040,102,1,1038,1043,1002,1037,1,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,102,1,1035,1040,1001,1038,0,1043,1002,1037,1,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,5,1032,1006,1032,165,1008,1040,35,1032,1006,1032,165,1102,1,2,1044,1106,0,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,38,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,1001,1039,0,1034,1001,1040,0,1035,101,0,1041,1036,102,1,1043,1038,1002,1042,1,1037,4,1044,1106,0,0,4,26,16,55,25,8,4,99,2,21,20,20,56,26,97,81,12,2,4,9,32,7,49,54,5,18,81,16,7,88,4,23,30,66,17,31,27,29,34,26,81,62,27,81,41,84,12,53,90,79,37,22,45,27,17,39,76,1,55,58,44,20,18,57,57,20,76,47,20,44,88,26,43,36,79,12,68,30,19,71,27,21,18,75,18,9,56,29,15,84,8,74,93,1,35,91,39,32,86,9,97,54,4,22,59,13,61,31,19,97,26,82,35,73,23,77,71,59,26,76,78,73,34,85,67,26,1,66,91,79,26,95,5,75,99,29,14,23,26,8,66,97,55,21,25,49,17,99,71,37,62,21,45,46,13,29,30,24,31,63,99,12,12,63,10,64,2,76,3,8,37,94,33,12,47,65,35,65,60,12,88,8,10,49,36,12,14,4,43,82,19,16,51,52,20,17,43,18,33,49,19,93,49,29,86,10,31,92,90,44,26,97,8,63,70,81,28,17,80,23,22,79,56,33,67,61,91,37,4,83,77,16,6,8,33,66,92,46,8,34,23,81,3,93,14,23,72,20,91,16,62,79,7,27,81,10,11,44,65,24,66,77,31,12,53,15,50,84,24,70,29,62,50,5,3,88,13,52,85,42,4,15,39,82,65,18,15,58,37,71,10,13,90,98,29,59,52,3,22,13,59,91,29,23,79,1,7,24,80,79,37,31,77,17,11,64,10,9,8,74,97,6,74,35,73,44,68,29,97,3,45,73,30,28,80,9,48,73,76,7,3,77,83,8,12,41,62,44,10,21,27,74,32,95,73,4,47,71,6,67,17,57,10,67,5,25,74,18,24,57,7,61,66,4,51,14,7,44,29,79,74,11,6,49,75,32,3,98,89,63,5,15,5,74,78,37,7,77,3,13,47,9,33,76,22,47,6,72,12,35,75,39,25,87,83,37,19,91,25,45,22,30,54,83,74,22,71,19,3,3,85,74,37,95,26,67,46,10,12,96,44,50,32,90,3,28,56,24,43,4,1,65,5,9,50,22,44,88,9,48,59,21,24,54,11,35,53,28,7,82,32,24,17,45,88,34,72,95,17,9,39,29,4,55,66,95,22,62,15,71,11,39,51,37,86,49,20,10,63,31,66,59,15,55,93,3,11,28,54,30,41,20,92,7,3,12,54,49,14,33,56,89,21,26,67,20,93,7,64,3,31,60,23,51,36,30,57,20,14,28,88,4,6,69,33,65,98,35,96,80,49,25,68,78,97,30,63,35,73,89,32,64,69,10,68,96,19,89,71,41,32,31,30,90,5,71,20,53,36,51,23,87,19,25,15,34,15,48,19,25,33,14,50,64,11,96,19,34,14,44,33,29,40,16,50,90,22,34,44,17,64,63,18,86,57,29,44,22,98,16,41,20,99,34,14,51,11,4,84,91,66,27,49,6,58,34,95,62,6,45,53,27,72,4,12,40,43,17,41,93,27,30,70,31,47,87,26,64,9,63,59,73,9,11,97,35,56,73,23,58,9,49,13,88,1,87,13,54,21,94,13,69,16,39,2,10,64,13,10,19,96,2,23,1,60,99,47,12,61,37,13,70,24,48,91,7,33,51,10,25,88,33,69,29,98,16,16,60,5,29,44,17,21,41,62,65,8,61,84,27,42,78,72,23,98,16,76,98,77,37,19,49,37,93,83,97,1,63,9,63,27,66,34,74,87,58,3,90,4,48,51,67,32,66,9,56,9,44,1,67,24,49,29,58,20,70,32,73,27,82,0,0,21,21,1,10,1,0,0,0,0,0,0"""
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

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

current_position = Point(x=0, y=0)
directions = {
    1: up,
    2: down,
    3: left,
    4: right
}

def add_point(p: Point, q: Point):
    return Point(p.x + q.x, p.y + q.y)

empty_spaces = { Point(x=0, y=0) }
wall_spaces = set()

def pop_next(dict):
    min_key = min(dict)
    set_value = dict[min_key]
    return_value = set_value.pop()
    if len(set_value) == 0:
        dict.pop(min_key, None)
    return return_value, min_key


def find_shortest_dist(start: Point, target: Point) -> int:
    places_to_explore = {
        0: { start }
    }
    seen_places = set()

    while len(places_to_explore) > 0:
        pos, dist = pop_next(places_to_explore)
        seen_places.add(pos)
        if pos == target:
            return dist
        for direction in directions.values():
            next_pos = add_point(pos, direction)
            if next_pos in wall_spaces:
                continue
            if next_pos in seen_places:
                # already visited
                continue
            if dist + 1 not in places_to_explore:
                places_to_explore[dist + 1] = set()
            places_to_explore[dist + 1].add(next_pos)
    # No more places to explore
    return -1


def find_direction_to_nearest_unknown() -> int:
    places_to_explore = {
        1: [ [(current_position, None)] ]
    }

    while len(places_to_explore) > 0:
        path, dist = pop_next(places_to_explore)
        for d, direction in directions.items():
            next_pos = add_point(path[-1][0], direction)
            if next_pos in wall_spaces:
                continue
            if next_pos in [p[0] for p in path]:
                # already visited
                continue
            if next_pos not in empty_spaces:
                return path[1][1]
            if dist + 1 not in places_to_explore:
                places_to_explore[dist + 1] = []
            places_to_explore[dist + 1].append(path + [(next_pos, d)])
    # No more places to explore
    return -1

target = None
while True:
    # Decide which way to go
    choosen_d = None
    for d, direction in directions.items():
        new_pos = add_point(current_position, direction)
        if new_pos in empty_spaces or new_pos in wall_spaces:
            continue
        else:
            choosen_d = d
            break
    if choosen_d is None:
        # we know everything around the robot.
        choosen_d = find_direction_to_nearest_unknown()
    assert(choosen_d is not None)

    if choosen_d == -1:
        # cannot find any new places to explore
        break

    # tell robot to go that way
    c.put_input(choosen_d)
    while not c.halted and not c.waiting_for_input and not c.has_output():
        c.run_step()
    if not c.has_output():
        print("Uh oh")
        exit(1)
    response = c.pop_next_output()

    if response == 0:
        wall_spaces.add(add_point(current_position, directions[choosen_d]))
    elif response == 1:
        current_position = add_point(current_position, directions[choosen_d])
        empty_spaces.add(current_position)
    elif response == 2:
        current_position = add_point(current_position, directions[choosen_d])
        empty_spaces.add(current_position)
        target = current_position
    else:
        print("Unknown response")
        exit(1)

print(find_shortest_dist(Point(0,0), target))

#
# r = 30
# for y in range(current_position.y - r, current_position.y + r + 1):
#     row = []
#     for x in range(current_position.x - r, current_position.x + r + 1):
#         p = Point(x, y)
#         if p == Point(0,0):
#             row.append("S")
#         elif p == target:
#             row.append("+")
#         elif p == current_position:
#             row.append("X")
#         elif p in wall_spaces:
#             row.append("#")
#         elif p in empty_spaces:
#             row.append(".")
#         else:
#             row.append(" ")
#     print("".join(row))
# print("---------")
# print("fin")


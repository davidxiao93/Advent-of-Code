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
        elif opcode == "read-input_string":
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


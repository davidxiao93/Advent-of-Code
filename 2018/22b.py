

from collections import namedtuple
from typing import List

Point = namedtuple("Point", ["x", "y"])

up = Point(x = 0, y = -1)
down = Point(x = 0, y = 1)
left = Point(x = -1, y = 0)
right = Point(x = 1, y = 0)

def add_point(p: Point, q: Point):
    return Point(p.x + q.x, p.y + q.y)


geologic_index_dict = {}
erosion_level_dict = {}
type_dict = {}

ROCKY = "rocky"
WET = "wet"
NARROW = "narrow"

TORCH = "torch"
CLIMBING_GEAR = "climbing_gear"
NEITHER = "neither"

def get_geologic_index(p: Point) -> int:
    if p in geologic_index_dict:
        return geologic_index_dict[p]

    if p.x == 0 and p.y == 0:
        geologic_index_dict[p] = 0
    elif p.x == target.x and p.y == target.y:
        geologic_index_dict[p] = 0
    elif p.y == 0:
        geologic_index_dict[p] = p.x * 16807
    elif p.x == 0:
        geologic_index_dict[p] = p.y * 48271
    else:
        geologic_index_dict[p] = get_erosion_level(
            add_point(p, Point(-1, 0))
        ) * get_erosion_level(
            add_point(p, Point(0, -1))
        )
    return geologic_index_dict[p]

def get_erosion_level(p: Point) -> int:
    if p in erosion_level_dict:
        return erosion_level_dict[p]

    geologic_index = get_geologic_index(p)
    erosion_level = (geologic_index + depth) % 20183
    erosion_level_dict[p] = erosion_level
    return erosion_level_dict[p]

def get_type(p: Point) -> int:
    if p in type_dict:
        return type_dict[p]
    type_int = get_erosion_level(p) % 3
    if type_int == 0:
        type = ROCKY
    elif type_int == 1:
        type = WET
    else:
        type = NARROW
    type_dict[p] = type
    return type_dict[p]

start = Point(0, 0)
target = Point(10, 715)
depth = 3339

equipments = [TORCH, CLIMBING_GEAR, NEITHER]

def valid_equipement_at(p: Point) -> List[str]:
    if p.x < 0 or p.y < 0:
        return []
    type = get_type(p)
    if type == ROCKY:
        return [CLIMBING_GEAR, TORCH]
    if type == WET:
        return [CLIMBING_GEAR, NEITHER]
    if type == NARROW:
        return [TORCH, NEITHER]
    print("Unknown type")
    exit(1)

def pop_next(dict):
    min_key = min(dict)
    set_value = dict[min_key]
    return_value = set_value.pop()
    if len(set_value) == 0:
        dict.pop(min_key, None)
    return return_value, min_key

# Maps time taken to state
time_mapping = {
    0: { (start, TORCH) }
}
visited_states = set()

reached_end = False
while not reached_end:
    (position, current_equipment), time_taken = pop_next(time_mapping)
    if position == target and current_equipment == TORCH:
        print(time_taken)
        exit(0)

    if (position, current_equipment) in visited_states:
        # already been here
        continue
    visited_states.add((position, current_equipment))

    # work out which ways I could go form position.
    # 1. I could switch equipment
    for e in valid_equipement_at(position):
        if e == current_equipment:
            continue
        if time_taken + 7 not in time_mapping:
            time_mapping[time_taken + 7] = set()
        time_mapping[time_taken + 7].add((position, e))
    # 2. I could try to move
    for d in [up, right, down, left]:
        new_pos = add_point(position, d)
        if current_equipment in valid_equipement_at(new_pos):
            if time_taken + 1 not in time_mapping:
                time_mapping[time_taken + 1] = set()
            time_mapping[time_taken + 1].add((new_pos, current_equipment))

print("wtf, this should not be printed")











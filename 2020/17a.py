from typing import Set

import file_loader

input_string = file_loader.get_input()

# input_string = """.#.
# ..#
# ###"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "z"])

def add_point(p: Point, q: Point):
    return Point(x = p.x + q.x, y = p.y + q.y, z = p.z + q.z)


active_cells = set()

# parse input_string
for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        if c == "#":
            active_cells.add(Point(x, y, 0))

# neighbour helpers
neighbours = [
    Point(x, y, z)
    for x in range(-1, 2)
    for y in range(-1, 2)
    for z in range(-1, 2)
    if x != 0 or y != 0 or z != 0
]

def get_neighbours(p: Point) -> Set[Point]:
    return { add_point(p, n) for n in neighbours }


def get_neighbours_of_active(active: Set[Point]) -> Set[Point]:
    neighbours_of_active = set()
    for a in active:
        a_neighbours = get_neighbours(a)
        for n in a_neighbours:
            if n not in active:
                neighbours_of_active.add(n)

    return neighbours_of_active

def get_num_active_neighbours(p: Point, active: Set[Point]) -> int:
    count = 0
    for n in get_neighbours(p):
        if n in active:
            count += 1
    return count

def will_be_active(p: Point, active: Set[Point]) -> bool:
    active_neighbours = get_num_active_neighbours(p, active)
    if p in active:
        if active_neighbours == 2 or active_neighbours == 3:
            return True
        else:
            return False
    if active_neighbours == 3:
        return True
    return False

def build_next_state(active: Set[Point]) -> Set[Point]:
    points_to_consider = get_neighbours_of_active(active) | active
    new_active = set()
    for p in points_to_consider:
        if will_be_active(p, active):
            new_active.add(p)

    return new_active


for i in range(6):
    active_cells = build_next_state(active_cells)

print(len(active_cells))


def pretty_print(active: Set[Point]):
    min_x = min(active, key=lambda a: a.x).x
    max_x = max(active, key=lambda a: a.x).x
    min_y = min(active, key=lambda a: a.y).y
    max_y = max(active, key=lambda a: a.y).y
    min_z = min(active, key=lambda a: a.z).z
    max_z = max(active, key=lambda a: a.z).z

    print(len(active))

    for z in range(min_z, max_z + 1):
        print(f"z={z}")
        for y in range(min_y, max_y + 1):
            row = []
            for x in range(min_x, max_x + 1):
                if Point(x, y, z) in active:
                    row.append("#")
                else:
                    row.append(".")
            print("".join(row))
        print("")



# pretty_print(active_cells)




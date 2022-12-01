from typing import Set, Dict

import file_loader

input_string = file_loader.get_input()

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x = 0, y = -1)
down = Point(x = 0, y = 1)
left = Point(x = -1, y = 0)
right = Point(x = 1, y = 0)
directions = [up, left, right, down] # reading order!

def add_point(p: Point, q: Point):
    return Point(x = p.x + q.x, y = p.y + q.y)


world = {}
for y, row in enumerate(input_string.splitlines()):
    for x, c in enumerate(row):
        if c == "#":
            world[Point(x, y)] = True
        else:
            world[Point(x, y)] = False

def get_neighbours(point: Point, world: Dict[Point, bool]) -> int:
    count = 0
    for d in directions:
        new_p = add_point(point, d)
        if new_p in world and world[new_p]:
            count += 1
    return count

def do_minute(world: Dict[Point, bool]) -> Dict[Point, bool]:
    points_to_change = set()
    points_to_consider = set()
    for point in world:
        if world[point]:
            points_to_consider.add(point)
            for d in directions:
                new_p = add_point(point, d)
                if new_p in world:
                    points_to_consider.add(new_p)
    for p in points_to_consider:
        bug_neighbours = get_neighbours(p, world)
        if world[p] and bug_neighbours != 1:
            points_to_change.add(p)
        elif not world[p] and (bug_neighbours == 1 or bug_neighbours == 2):
            points_to_change.add(p)
    for p in points_to_change:
        world[p] = not world[p]

    return world

def get_state(world: Dict[Point, bool]) -> str:
    rows = []
    for y in range(5):
        row = []
        for x in range(5):
            row.append(
                "#" if world[Point(x, y)] else "."
            )
        rows.append("".join(row))
    return "\n".join(rows)

import math

seen_states = { get_state(world) }
minute = 0
while True:
    world = do_minute(world)
    minute += 1
    new_state = get_state(world)
    if new_state in seen_states:
        total_biodiversity = 0
        for p, v in world.items():
            if not v:
                continue
            total_biodiversity += int(math.pow(2, 5*p.y + p.x))
        print(total_biodiversity)
        break
    seen_states.add(new_state)











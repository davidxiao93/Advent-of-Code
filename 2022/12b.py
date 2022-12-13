from typing import Dict, List

import file_loader

from collections import namedtuple

input_string = file_loader.get_input()

Point = namedtuple("Point", ["x", "y"])

height_map: Dict[Point, int] = dict()
start: Point = Point(0,0)
potential_ends = []
"""
Instead of searching from each 'a' to 'E', I'll bfs backwards from 'E' to the first 'a'
"""

for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        if c == "S":
            c = "a"
        elif c == "E":
            start = Point(x, y)
            c = "z"
        if c == "a":
            potential_ends.append(Point(x, y))
        height_map[Point(x, y)] = ord(c) - ord("a")

def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)

directions = [
    Point(0, 1),
    Point(1, 0),
    Point(-1, 0),
    Point(0, -1)
]

steps: Dict[Point, int] = {
    start: 0
}

paths: Dict[int, List[Point]] = {
    0: [start]
}

def pop_next(c):
    min_key = min(c)
    states = c[min_key]
    return_value = states[0]
    states.pop(0)
    if len(states) == 0:
        c.pop(min_key, None)
    return min_key, return_value

while True:
    current_steps, p = pop_next(paths)
    current_height = height_map[p]
    for d in directions:
        new_p = add_point(p, d)
        if new_p not in height_map:
            continue
        new_height = height_map[new_p]
        if new_height < current_height - 1:
            # too far below, would need climbing gear on the way up
            continue
        if new_height == 0:
            # Found the bottom
            print(current_steps + 1)
            exit()
        if new_p not in steps or steps[new_p] > current_steps + 1:
            steps[new_p] = current_steps + 1
            if current_steps + 1 not in paths:
                paths[current_steps + 1] = []
            paths[current_steps + 1].append(new_p)

from typing import Set

import file_loader

input_string = file_loader.get_input()

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)

directions = {
    "U": Point(0, -1),
    "R": Point(1, 0),
    "D": Point(0, 1),
    "L": Point(-1, 0)
}

def parse_line(line: str) -> Set[Point]:
    points = set()
    current_pos = Point(0, 0)
    movements = line.split(",")
    for movement in movements:
        d = directions[movement[0]]
        for i in range(int(movement[1:])):
            current_pos = add_point(current_pos, d)
            points.add(current_pos)
    return points

line_0 = parse_line(input_string.splitlines()[0])
line_1 = parse_line(input_string.splitlines()[1])

crossing_points = line_0.intersection(line_1)

print(min([abs(c.x) + abs(c.y) for c in crossing_points]))

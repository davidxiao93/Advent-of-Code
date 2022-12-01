from typing import Set, Dict

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

def parse_line(line: str) -> Dict[Point, int]:
    points = {}
    current_pos = Point(0, 0)
    steps = 0
    movements = line.split(",")
    for movement in movements:
        d = directions[movement[0]]
        for i in range(int(movement[1:])):
            current_pos = add_point(current_pos, d)
            steps += 1
            if current_pos not in points:
                points[current_pos] = steps
    return points

line_0 = parse_line(input_string.splitlines()[0])
line_1 = parse_line(input_string.splitlines()[1])

crossing_points = set(line_0.keys()).intersection(set(line_1.keys()))

print(min([
    line_0[c] + line_1[c]
    for c in crossing_points
]))




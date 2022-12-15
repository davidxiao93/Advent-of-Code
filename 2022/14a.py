from typing import Set

import file_loader
from collections import namedtuple

input_string = file_loader.get_input()

Point = namedtuple("Point", ["x", "y"])

points: Set[Point] = set()

for line in input_string.splitlines():
    steps = [Point(int(p.split(",")[0].strip()), int(p.split(",")[1].strip())) for p in line.split("->")]

    for i in range(len(steps) - 1):
        from_step = steps[i]
        to_step = steps[i + 1]
        if from_step.x == to_step.x:
            for j in range(min(from_step.y, to_step.y), max(from_step.y, to_step.y) + 1):
                points.add(Point(from_step.x, j))
        else:
            for j in range(min(from_step.x, to_step.x), max(from_step.x, to_step.x) + 1):
                points.add(Point(j, from_step.y))

start = Point(500,0)

max_y = max([p.y for p in points])

def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)

directions = [
    Point(0, 1),
    Point(-1, 1),
    Point(1, 1)
]

counter = 0
while True:
    sand = start
    counter += 1
    while True:
        moved = False
        for d in directions:
            new_sand = add_point(sand, d)
            if new_sand not in points:
                sand = new_sand
                moved = True
                break
        if not moved:
            points.add(sand)
            break
        if sand.y > max_y:
            # going into the endless void
            # minus one because counter includes the sand that has fallen into the void
            print(counter - 1)
            exit()











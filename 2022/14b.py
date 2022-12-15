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

min_x = min([p.x for p in points])
max_x = max([p.x for p in points])
max_y = max([p.y for p in points])

# Add floor
floor_y = max_y + 2
floor_min_X = min_x - floor_y - 10
floor_max_x = max_x + floor_y + 10
for j in range(floor_min_X, floor_max_x + 1):
    points.add(Point(j, floor_y))

def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)

directions = [
    Point(0, 1),
    Point(-1, 1),
    Point(1, 1)
]

counter = 0
while start not in points:
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

print(counter)











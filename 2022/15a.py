from typing import Set, List, Dict
from collections import namedtuple
import file_loader

input_string = file_loader.get_input()
y = 2_000_000

Point = namedtuple("Point", ["x", "y"])

def manhattan(p: Point, q: Point) -> int:
    return abs(p.x - q.x) + abs(p.y - q.y)

def getManhattanPoints(p: Point, d: int) -> Set[int]:
    return {
        x
        for x in range(p.x - d + abs(p.y - y), p.x + d + 1 - abs(p.y - y))
    }

sensors: Dict[Point, Point] = dict()
for line in input_string.splitlines():
    sensors[
        Point(
            x = int(line.split()[2].split("=")[1][:-1]),
            y = int(line.split()[3].split("=")[1][:-1])
        )
    ] = Point(
        x = int(line.split()[-2].split("=")[1][:-1]),
        y = int(line.split()[-1].split("=")[1])
    )

points: Set[int] = set()

for sensor, beacon in sensors.items():
    distance = manhattan(sensor, beacon)
    points = points.union(getManhattanPoints(sensor, distance))

points = (points - {sensor.x for sensor in sensors.keys() if sensor.y == y}) - {sensors[sensor].x for sensor in sensors.keys() if sensors[sensor].y == y}

print(len(points))

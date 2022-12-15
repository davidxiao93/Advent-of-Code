from typing import Set, List, Dict
from collections import namedtuple
import file_loader

input_string = file_loader.get_input()
r = 4_000_000

# input_string = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
# r = 20

Point = namedtuple("Point", ["x", "y"])

def manhattan(p: Point, q: Point) -> int:
    return abs(p.x - q.x) + abs(p.y - q.y)

sensors: Dict[Point, int] = dict()
beacons: Set[Point] = set()
for line in input_string.splitlines():
    sensor = Point(
        x = int(line.split()[2].split("=")[1][:-1]),
        y = int(line.split()[3].split("=")[1][:-1])
        )
    beacon = Point(
        x = int(line.split()[-2].split("=")[1][:-1]),
        y = int(line.split()[-1].split("=")[1])
    )
    beacons.add(beacon)
    sensors[sensor] = manhattan(sensor, beacon)


def isDistress(p: Point) -> bool:
    for s in sensors.keys():
        if manhattan(s, p) <= sensors[s]:
            return False
    return True

# Gets the set of points that is beacon_distance + 1 away from sensor
# We know that there is exactly one distress beacon, so it must lie just outside the boundary of one of the sensors
def surroundingPoints(sensor: Point, beacon_distance: int) -> List[Point]:
    return [
        Point(sensor.x + i, sensor.y + (beacon_distance + 1 - i))
        for i in range(beacon_distance + 2)
    ] + [
        Point(sensor.x - i, sensor.y - (beacon_distance + 1 - i))
        for i in range(beacon_distance + 2)
    ] + [
        Point(sensor.x - i, sensor.y + (beacon_distance + 1 - i))
        for i in range(beacon_distance + 2)
    ] + [
        Point(sensor.x + i, sensor.y - (beacon_distance + 1 - i))
        for i in range(beacon_distance + 2)
    ]

for sensor in sensors.keys():
    for p in surroundingPoints(sensor, sensors[sensor]):
        if 0 <= p.x <= r and 0 <= p.y <= r and p not in sensors.keys() and p not in beacons and isDistress(p):
            tuning = 4_000_000 * p.x + p.y
            print(tuning)
            exit()


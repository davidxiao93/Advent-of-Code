from __future__ import annotations
from collections import namedtuple
from typing import Set

import file_loader

input_string = file_loader.get_input()

class Point(namedtuple('Point', ['x', 'y'])):
    def __add__(self: Point, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __radd__(self: Point, other: Point) -> Point:
        return self + other

    def __sub__(self: Point, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __rsub__(self: Point, other: Point) -> Point:
        return -self + other

    def __neg__(self: Point) -> Point:
        return Point(-self.x, -self.y)

    def __mul__(self: Point, other: int) -> Point:
        return Point(self.x*other, self.y*other)

    def __rmul__(self: Point, other: int) -> Point:
        return self * other

    def __len__(self: Point) -> int:
        return abs(self.x) + abs(self.y)

    def __repr__(self: Point) -> str:
        return f"({self.x}, {self.y})"

    def __str__(self: Point) -> str:
        return f"({self.x}, {self.y})"

    def __lt__(self: Point, other: Point) -> bool:
        return self.x < other.x or self.y < other.y

    def __eq__(self: Point, other: Point) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self: Point) -> int:
        return hash(tuple((self.x, self.y)))

class Door:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def __eq__(self, other: Door):
        return (self.a == other.a and self.b == other.b) or (self.b == other.a and self.a == other.b)

    def __hash__(self):
        return hash(tuple(sorted([self.a, self.b])))

    def __str__(self) -> str:
        return f"({self.a} to {self.b})"

    def __repr__(self):
        return self.__str__()



# returns the list of endpoints that is reached at the end of the remaining_regex
def grid(start: Point, remaining_regex: str, doors: Set[Door]) -> Set[Point]:
    if len(remaining_regex) == 0:
        return { start }
    i = 0
    p = start
    while i < len(remaining_regex) and remaining_regex[i] != "(":
        c = remaining_regex[i]
        if c == "N":
            new_p = p + Point(0, -1)
        elif c == "E":
            new_p = p + Point(1, 0)
        elif c == "S":
            new_p = p + Point(0, 1)
        elif c == "W":
            new_p = p + Point(-1, 0)
        else:
            print("Wtf")
            new_p = None # shut up the linter
            exit(1)
        doors.add(Door(p, new_p))
        p = new_p
        i += 1
    if i == len(remaining_regex):
        # no brackets
        return { p }

    remaining_regex = remaining_regex[i:]
    # remaining regex now starts with a bracket
    assert(remaining_regex[0] == "(")
    nesting = 1
    i = 1
    splits = []
    current_split = ""
    while nesting != 0:
        c = remaining_regex[i]

        if c == "(":
            nesting += 1
        elif c == ")":
            nesting -= 1

        if c == "|" and nesting == 1:
            splits.append(current_split)
            current_split = ""
        else:
            current_split += c

        i += 1
    splits.append(current_split[:-1])
    br = i - 1
    remaining_regex = remaining_regex[br + 1:]

    new_starts = set()
    for part in splits:
        new_starts |= grid(p, part, doors)

    return_starts = set()
    for new_start in new_starts:
        return_starts |= grid(new_start, remaining_regex, doors)
    return return_starts


doors = set()
start = Point(0, 0)
remaining_regex = input_string[1:-1]

ends = grid(start, remaining_regex, doors)


def pretty_print(doors: Set[Door]):
    all_points = []
    for d in doors:
        all_points.append(d.a)
        all_points.append(d.b)
    upper_left = min(all_points)
    lower_right = max(all_points)
    print("#" * (((lower_right.x - upper_left.x + 1) * 2) + 1))
    for y in range(upper_left.y, lower_right.y + 1):
        s = ["#"]
        for x in range(upper_left.x, lower_right.x + 1):
            s.append(
                "X" if x == 0 and y == 0 else "."
            )
            s.append(
                "|" if Door(Point(x, y), Point(x+1, y)) in doors else "#"
            )
        print("".join(s))
        s = []
        for x in range(upper_left.x, lower_right.x + 1):
            s.append(
                "-" if Door(Point(x, y), Point(x, y + 1)) in doors else "#"
            )
        print("#" + "#".join(s) + "#")



def find_distances(doors: Set[Door]):
    all_points = set()
    for d in doors:
        all_points.add(d.a)
        all_points.add(d.b)
    upper_left = min(all_points)
    lower_right = max(all_points)

    distances = {}

    points_to_consider = { (Point(x=0, y=0), 0) }
    while len(points_to_consider) > 0:
        next_point, dist = points_to_consider.pop()
        if next_point not in all_points:
            # not interested in this place
            continue
        if next_point in distances:
            # already visited. no point coming back here
            continue
        distances[next_point] = dist
        for d in [Point(1, 0), Point(-1, 0), Point(0, 1), Point(0, -1)]:
            new_point = next_point + d
            if Door(next_point, new_point) in doors:
                points_to_consider.add((new_point, dist + 1))

    return distances


distances = find_distances(doors)

print(max(distances.values()))
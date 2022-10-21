from typing import Set, Dict

input = """..##.
..#..
##...
#....
...##"""

from collections import namedtuple

Point = namedtuple("Point", ["l", "x", "y"])
up = Point(l = 0, x = 0, y = -1)
down = Point(l = 0, x = 0, y = 1)
left = Point(l = 0, x = -1, y = 0)
right = Point(l = 0, x = 1, y = 0)
directions = [up, left, right, down]

def add_point(p: Point, q: Point):
    return Point(l = p.l + q.l, x = p.x + q.x, y = p.y + q.y)


bugs = set()
for y, row in enumerate(input.splitlines()):
    for x, c in enumerate(row):
        if c == "#":
            bugs.add(Point(0,x, y))

def get_neighbours(point: Point) -> Set[Point]:
    neighbours = set()
    for d in directions:
        new_p = add_point(point, d)
        if new_p.x == 2 and new_p.y == 2:
            if d == left:
                for i in range(5):
                    neighbours.add(Point(point.l - 1, 4, i))
            elif d == down:
                for i in range(5):
                    neighbours.add(Point(point.l - 1, i, 0))
            elif d == up:
                for i in range(5):
                    neighbours.add(Point(point.l - 1, i, 4))
            else:
                for i in range(5):
                    neighbours.add(Point(point.l - 1, 0, i))
        else:
            if new_p.x < 0:
                neighbours.add(Point(point.l + 1, 1, 2))
            elif new_p.y < 0:
                neighbours.add(Point(point.l + 1, 2, 1))
            elif new_p.x > 4:
                neighbours.add(Point(point.l + 1, 3, 2))
            elif new_p.y > 4:
                neighbours.add(Point(point.l + 1, 2, 3))
            else:
                neighbours.add(new_p)
    return neighbours

def do_minute(bugs: Set[Point]) -> Set[Point]:
    points_to_change = set()
    points_to_consider = set()
    for bug in bugs:
        points_to_consider.add(bug)
        points_to_consider |= get_neighbours(bug)
    for p in points_to_consider:
        bug_neighbours = len([n for n in get_neighbours(p) if n in bugs])
        if p in bugs and bug_neighbours != 1:
            points_to_change.add(p)
        elif p not in bugs and (bug_neighbours == 1 or bug_neighbours == 2):
            points_to_change.add(p)
    for p in points_to_change:
        if p in bugs:
            bugs.remove(p)
        else:
            bugs.add(p)

    return bugs

def pretty_print(bugs: Set[Point]):
    min_layer = min(bugs, key=lambda p: p.l).l
    max_layer = max(bugs, key=lambda p: p.l).l
    for l in range(min_layer, max_layer + 1):
        print("Depth", l)
        for y in range(5):
            row = []
            for x in range(5):
                if Point(l, x, y) in bugs:
                    row.append("#")
                else:
                    row.append(".")
            print("".join(row))
        print("\n")





for j in range(200):
    bugs = do_minute(bugs)

print(len(bugs))










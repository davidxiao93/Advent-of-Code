import file_loader

input_string = file_loader.get_input()

# input_string = """x=495, y=2..7
# y=7, x=495..501
# x=501, y=3..7
# x=498, y=2..4
# x=506, y=1..2
# x=498, y=10..13
# x=504, y=10..13
# y=13, x=498..504"""


from collections import namedtuple
from typing import Set, Dict, Tuple, List

Point = namedtuple("Point", ["x", "y"])

def add_point(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)


up = Point(x = 0, y = -1)
down = Point(x = 0, y = 1)
left = Point(x = -1, y = 0)
right = Point(x = 1, y = 0)
directions = [up, right, down, left]

clays: Set[Point] = set()
waters: Set[Point] = set()

WATER_REACHABLE = "|"
WATER_SETTLED = "~"
CLAY = "#"
SAND = "."



for line in input_string.splitlines():
    left_str, right_str = line.split(", ")
    leftc, leftv = left_str.split("=")
    rightc, rightv = right_str.split("=")
    right_lower, right_upper = rightv.split("..")
    xs = set()
    ys = set()
    if leftc == "x":
        xs = {int(leftv)}
    else:
        ys = {int(leftv)}

    if rightc == "x":
        xs = { i for i in range(int(right_lower), int(right_upper) + 1)}
    else:
        ys = { i for i in range(int(right_lower), int(right_upper) + 1)}
    for x, y in [(x, y) for x in xs for y in ys]:
        clays.add(Point(x, y))

# build grid
max_x = max(clays, key=lambda p: p.x).x
max_y = max(clays, key=lambda p: p.y).y
min_x = min(clays, key=lambda p: p.x).x
min_y = min(clays, key=lambda p: p.y).y
grid = []
for y in range(max_y + 5):
    grid.append([SAND] * (max_x + 5))
for p in clays:
    grid[p.y][p.x] = CLAY

def read_grid(position: Point, grid):
    if position.y < 0:
        print("wtf")
        exit(1)
    return grid[position.y][position.x]

def write_grid(position: Point, grid, v):
    grid[position.y][position.x] = v

def pretty_print(focus: Point, grid):
    for y in range(max(0, focus.y - 10), min(len(grid), focus.y + 50)):
        row = [str(y).zfill(4)]
        for x in range(max(0, focus.x - 70), min(len(grid[0]), focus.x + 70)):
            if y == 0 and x == 500:
                row.append("+")
            elif y == focus.y and x == focus.x:
                row.append("X")
            else:
                row.append(read_grid(Point(x, y), grid))
        print(" ".join(row))

def is_supported(position, grid):
    below_state = read_grid(add_point(position, down), grid)
    return below_state == CLAY or below_state == WATER_SETTLED



def fill_layer(start: Point, grid) -> Set[Point]:
    # Returns set of new starting points
    # Empty set means no new starting points
    new_starting_points = set()
    maybe_settled = { start }
    for d in [left, right]:
        d_pos = start
        while is_supported(d_pos, grid) \
                and (read_grid(add_point(d_pos, d), grid) == SAND
                        or read_grid(add_point(d_pos, d), grid) == WATER_REACHABLE):
            d_pos = add_point(d_pos, d)
            maybe_settled.add(d_pos)
        if is_supported(d_pos, grid):
            # obstacle must be found
            pass
        else:
            # overhang found
            new_starting_points.add(d_pos)

    if len(new_starting_points) == 0:
        for p in maybe_settled:
            write_grid(p, grid, WATER_SETTLED)
    else:
        for p in maybe_settled:
            write_grid(p, grid, WATER_REACHABLE)
    return new_starting_points

def fill_container(start: Point, grid) -> Set[Point]:
    assert(is_supported(start, grid))
    # One of two things can happen.
    # - We go up one layer to fill it
    # - We spill
    new_starting_points = fill_layer(start, grid)
    while len(new_starting_points) == 0:
        start = add_point(start, up)
        new_starting_points = fill_layer(start, grid)
    return new_starting_points

def fall_down(start: Point, grid) -> Set[Point]:

    while not is_supported(start, grid):
        if start.y + 2 >= len(grid):
            # fallen off the grid
            return set()
        write_grid(start, grid, WATER_REACHABLE)
        start = add_point(start, down)

    # start is now supported.
    return fill_container(start, grid)


start = Point(500, 0)
seen_starting_points = { start }
start_points = [ start ]

while len(start_points) != 0:
    next_start = start_points.pop()
    new_starts = fall_down(next_start, grid)
    for n in new_starts:
        if n not in seen_starting_points:
            start_points.append(n)
            seen_starting_points.add(n)


def count_water_reachable(grid):
    count = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x - 2, max_x + 3):
            v = read_grid(Point(x, y), grid)
            if v == WATER_SETTLED:
                count += 1
    return count

print(count_water_reachable(grid))




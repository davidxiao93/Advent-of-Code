from typing import Set, List, Callable

import file_loader

input_string = file_loader.get_input()

"""
Confession: I did take a look at 
https://www.reddit.com/r/adventofcode/comments/aa9uvg/day_23_aoc_creators_logic/
after 5 days of thinking about this problem and without wanting to use off the shelf libraries

Admittedly, I had come up with ideas similar to using octrees, but mine are far less practical
(My idea was rather than dividing the space into 8 (two in each dimension) I would "lower" the 
resolution of each coordinate (e.g. x coord of 123456789 would become 123457 for a factor of 1000) 
by some factor and then introduce some fuzzyness to account for the rounding. 
Definitely less practical and fiddly to implement)
"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "z"])
Nanobot = namedtuple("Nanobot", ["p", "r"])
Cube = namedtuple("Cube", ["a", "b"]) # a.x <= b.x and a.y <= b.y and a.z <= b.z

nanobots = []
for line in input_string.splitlines():
    pos_str, r_str = line.split(", ")
    r = int(r_str[2:])
    x, y, z = (int(a) for a in pos_str[5:-1].split(",", 2))
    n = Nanobot(Point(x, y, z), r)
    nanobots.append(n)


def distance(p: Point, q: Point) -> int:
    return abs(p.x - q.x) + abs(p.y - q.y) + abs(p.z - q.z)

def split_cube(c: Cube) -> Set[Cube]:
    split_x = int((c.a.x + c.b.x) // 2)
    split_y = int((c.a.y + c.b.y) // 2)
    split_z = int((c.a.z + c.b.z) // 2)
    return {
        Cube(Point(xs[0], ys[0], zs[0]), Point(xs[1], ys[1], zs[1]))
        for xs in [(c.a.x, split_x), (min(split_x + 1, c.b.x), c.b.x)]
        for ys in [(c.a.y, split_y), (min(split_y + 1, c.b.y), c.b.y)]
        for zs in [(c.a.z, split_z), (min(split_z + 1, c.b.z), c.b.z)]
    }


def get_cube_distance_to_nanobot_one_dim(cube: Cube, nanobot: Nanobot, l: Callable[[Point], int]) -> int:
    a = l(cube.a)
    b = l(cube.b)
    n = l(nanobot.p)
    if n < a:
        return a - n
    if n > b:
        return n - b
    return 0


def get_cube_distance_to_nanobot(c: Cube, n: Nanobot) -> int:
    return sum([
        get_cube_distance_to_nanobot_one_dim(c, n, l)
        for l in [
            lambda p: p.x,
            lambda p: p.y,
            lambda p: p.z
        ]
    ])

def get_nanobots_in_range_of_cube(c: Cube, nanobots: List[Nanobot]) -> int:
    count = 0
    for n in nanobots:
        cube_distance = get_cube_distance_to_nanobot(c, n)
        if cube_distance <= n.r:
            count += 1
    return count


def is_cube_single_point(c: Cube) -> bool:
    return c.a.x == c.b.x and c.a.y == c.b.y and c.a.z == c.b.z

def cube_distance_to_origin(c: Cube) -> int:
    return int(distance(
        Point(0, 0, 0),
        Point((c.a.x + c.b.x) / 2, (c.a.y + c.b.y) / 2, (c.a.z + c.b.z) / 2)
    ))

candidate_cubes = {Cube(
    Point(-100_000_000, -100_000_000, -100_000_000),
    Point(100_000_000, 100_000_000, 100_000_000)
)}


while True:
    if all([is_cube_single_point(c) for c in candidate_cubes]):
        break
    max_in_range = 0
    max_in_range_cubes = set()
    cubes_to_check = set()
    for c in candidate_cubes:
        if is_cube_single_point(c):
            cubes_to_check |= {c}
        else:
            cubes_to_check |= split_cube(c)
    for c in cubes_to_check:
        count = get_nanobots_in_range_of_cube(c, nanobots)
        if count > max_in_range:
            max_in_range = count
            max_in_range_cubes = { c }
        elif count == max_in_range:
            max_in_range_cubes.add(c)
    candidate_cubes = max_in_range_cubes

print(cube_distance_to_origin(candidate_cubes.pop()))

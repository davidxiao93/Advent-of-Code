import file_loader

input_string = file_loader.get_input()

from typing import Dict, List, Set
from collections import namedtuple
Point = namedtuple("Point", ["w", "ne"])
def add_point(p: Point, q: Point) -> Point:
    return Point(w = p.w + q.w, ne = p.ne + q.ne)


conversion = {
    "w": Point(w=1, ne=0),
    "nw": Point(w=1, ne=1),
    "ne": Point(w=0, ne=1),
    "e": Point(w=-1, ne=0),
    "se": Point(w=-1, ne=-1),
    "sw": Point(w=0, ne=-1)
}

def get_coordinate(directions: List[str]) -> Point:
    current_point = Point(w = 0, ne = 0)
    for d in directions:
        current_point = add_point(current_point, conversion[d])
    return current_point

def parse_input(p: str) -> List[str]:
    directions = []
    candidates = ["e", "w", "nw", "ne", "sw", "se"]
    while len(p) > 0:
        for c in candidates:
            if p.startswith(c):
                directions.append(c)
                p = p[len(c):]
    return directions

flip_tiles = {}

for line in input_string.splitlines():
    coordinate = get_coordinate(parse_input(line))
    if coordinate not in flip_tiles:
        flip_tiles[coordinate] = 0
    flip_tiles[coordinate] += 1

black_tiles = { c for c, v in flip_tiles.items() if v % 2 == 1 }

def count_black_tile_neighbours(black_tiles: Set[Point], p: Point) -> int:
    count = 0
    for d in conversion.values():
        if add_point(p, d) in black_tiles:
            count += 1
    return count

def one_day(black_tiles: Set[Point]) -> Set[Point]:
    tiles_to_check = set()
    for t in black_tiles:
        tiles_to_check.add(t)
        for d in conversion.values():
            tiles_to_check.add(add_point(t, d))

    tiles_to_flip = set()
    for t in tiles_to_check:
        black_tile_neighbours = count_black_tile_neighbours(black_tiles, t)
        if t in black_tiles:
            if black_tile_neighbours == 0 or black_tile_neighbours > 2:
                tiles_to_flip.add(t)
        else:
            if black_tile_neighbours == 2:
                tiles_to_flip.add(t)
    for t in tiles_to_flip:
        if t in black_tiles:
            black_tiles.remove(t)
        else:
            black_tiles.add(t)

    return black_tiles


for i in range(100):
    black_tiles = one_day(black_tiles)

print(len(black_tiles))

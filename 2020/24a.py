import file_loader

input_string = file_loader.get_input()

from typing import Dict, List

simplifications = {
        ("e", "w"): [],
        ("ne", "sw"): [],
        ("nw", "se"): [],
        ("ne", "w"): ["nw"],
        ("nw", "e"): ["ne"],
        ("w", "se"): ["sw"],
        ("e", "sw"): ["se"],
        ("ne", "se"): ["e"],
        ("nw", "sw"): ["w"]
    }

def get_coordinate(directions: List[str]) -> str:
    path = {
        "w": 0,
        "nw": 0,
        "ne": 0,
        "e": 0,
        "se": 0,
        "sw": 0
    }
    for direction in directions:
        path[direction] += 1

    has_changed = True
    while has_changed:
        has_changed = False
        for (a, b), rs in simplifications.items():
            if path[a] > 0 and path[b] > 0:
                has_changed = True
                path[a] -= 1
                path[b] -= 1
                for r in rs:
                    path[r] += 1
        if sum(path.values()) == 0:
            break
    return ",".join([str(k) + ":" + str(path[k]) for k in sorted(path.keys())])

def parse_input(p: str) -> List[str]:
    directions = []
    candidates = ["e", "w", "nw", "ne", "sw", "se"]
    while len(p) > 0:
        for c in candidates:
            if p.startswith(c):
                directions.append(c)
                p = p[len(c):]
    return directions

flip_tiles = {

}

for line in input_string.splitlines():
    coordinate = get_coordinate(parse_input(line))
    if coordinate not in flip_tiles:
        flip_tiles[coordinate] = 0
    flip_tiles[coordinate] += 1

"""
want number of tiles that have been flipped an odd number of times
"""
print(sum([1 for v in flip_tiles.values() if v % 2 == 1]))



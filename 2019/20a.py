import file_loader

input_string = file_loader.get_input()
from collections import namedtuple
from typing import List, Dict, Set

Point = namedtuple("Point", ["x", "y"])
up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)
directions = [up, right, down, left]
def add_point(p: Point, q: Point):
    return Point(p.x + q.x, p.y + q.y)


portals: Dict[Point, str] = {}
walls: Set[Point] = set()
space: Set[Point] = set()
for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        if c == "#":
            walls.add(Point(x, y))
        elif c == ".":
            space.add(Point(x, y))
        elif c.isalpha():
            portals[Point(x, y)] = c

portal_neighbours: Dict[str, List[Point]] = {}
neighbours: Dict[Point, List[Point]] = {}
for s in space:
    # define neighbours
    neighbours[s]: List[Point] = []
    for d in directions:
        new_s = add_point(s, d)
        if new_s in space:
            neighbours[s].append(new_s)
        elif new_s in portals:
            new_new_s = add_point(new_s, d)
            assert(new_new_s in portals)
            portal_letters = "".join(sorted([portals[new_s], portals[new_new_s]]))
            if portal_letters not in portal_neighbours:
                portal_neighbours[portal_letters] = []
            portal_neighbours[portal_letters].append(s)

for _, points in portal_neighbours.items():
    if len(points) == 2: # only exceptions should be AA and ZZ
        neighbours[points[0]].append(points[1])
        neighbours[points[1]].append(points[0])

# neighbours is now fully defined
start = portal_neighbours["AA"][0]
target = portal_neighbours["ZZ"][0]



# standard bfs
def pop_next(dict):
    min_key = min(dict)
    set_value = dict[min_key]
    return_value = set_value.pop()
    if len(set_value) == 0:
        dict.pop(min_key, None)
    return return_value, min_key

step_mapping = {
    0: { start }
}
seen_positions = set()
while len(step_mapping) != 0:
    pos, dist = pop_next(step_mapping)
    if pos == target:
        print(dist)
        break
    if pos in seen_positions:
        continue
    seen_positions.add(pos)
    for n in neighbours[pos]:
        if dist + 1 not in step_mapping:
            step_mapping[dist + 1] = set()
        step_mapping[dist + 1].add(n)







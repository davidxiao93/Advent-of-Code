import file_loader

input_string = file_loader.get_input()
from collections import namedtuple
from typing import List, Dict, Set, Tuple

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
for s in space:
    for d in directions:
        new_s = add_point(s, d)
        if new_s in portals:
            new_new_s = add_point(new_s, d)
            assert(new_new_s in portals)
            portal_letters = "".join(sorted([portals[new_s], portals[new_new_s]]))
            if portal_letters not in portal_neighbours:
                portal_neighbours[portal_letters] = []
            portal_neighbours[portal_letters].append(s)
            break

portal_connections: Dict[Point, Point] = {}
for _, points in portal_neighbours.items():
    if len(points) == 2: # only exceptions should be AA and ZZ
        portal_connections[points[0]] = points[1]
        portal_connections[points[1]] = points[0]

start = (0, portal_neighbours["AA"][0])
target = (0, portal_neighbours["ZZ"][0])

def get_neighbours(layer: int, point: Point) -> List[Tuple[int, Point]]:
    return_list: List[Tuple[int, Point]] = []
    for d in directions:
        new_p = add_point(point, d)
        if new_p in space:
            return_list.append((layer, new_p))
    if point in portal_connections:
        if point.x == 2 \
                or point.y == 2 \
                or point.x == len(input_string.splitlines()[0]) - 3 \
                or point.y == len(input_string.splitlines()) - 3:
            if layer != 0:
                # going up a layer
                return_list.append((layer + 1, portal_connections[point]))
        else:
            return_list.append((layer - 1, portal_connections[point]))
    return return_list


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
    (layer, pos), dist = pop_next(step_mapping)
    if (layer, pos) == target:
        print(dist)
        break
    if (layer, pos) in seen_positions:
        continue
    seen_positions.add((layer, pos))
    for n_layer, n_pos in get_neighbours(layer, pos):
        if dist + 1 not in step_mapping:
            step_mapping[dist + 1] = set()
        step_mapping[dist + 1].add((n_layer, n_pos))







from typing import Dict, Set, Tuple

input = """#################################################################################
#.....#...............#.....#.A.#.......#.....#e..............#.....#...........#
#.###.#########.#####.###.#.###.#.###.#.###.#.###.###########.#.#.###.#####.#####
#.#.#.....#...#.#...#.#...#.....#.#.#.#.#...#..m#...#.......#.#.#.#...#.#...#...#
#.#.#####.#.#.#.#.###.#.#########.#.#.###.#####.###.#.#######.###.#.###.#N###.#.#
#.#.#...#...#...#...#.#.....T.......#...#.#...#.....#.#.....#.#...#.....#.#...#.#
#.#.#.#.###########.#.#.###############.#.#.#.#######.#.###.#.#.#.#####.#.#.###.#
#.#...#.......#.....#.#.......#.....#...#.#.#...#.........#j....#.#...#.#.#.#...#
#.###########.#.#.#.#.#########.###.#.#.#.#.###.#.#########.#####.###.#.#.#.#.#.#
#.#.....#...#.#.#.#.#...........#...#.#.#.#...#.#.#...#...#.#...#...#.#.#...#.#.#
#.#P###.#D#.#.#.#.###############.###.#.#.###.#.#.###.#.#.###.#.###.#.#.#####.###
#...#...#.#.#u..#.......#...#.....#...#.#.#...#.......#.#.....#...#...#.....#...#
#####.###.#.#######.###.#.###.#######.#.#.#########.###.#########.#########.###.#
#...#.#...#g......#...#.#...#.#.....#.#.#.#...#...#.#...#.......#.#.........#...#
#.#.#.#.#########.###.#.###.#.###.#.#.#.#.#.#.#.#.###.#######.#.#.#.#########O#.#
#.#...#..d#.....#...#.#.....#.....#...#.#...#...#.....#.....#.#.#...#.....#...#.#
#.#######.#.###F###.#.#################.#.###############.#.#.#.#######.#.#.###.#
#.....#...#..h#...#.#.............#.....#.#.......#.......#...#.....#...#.#.#...#
#.###.#H#####.#.###G#.#######.#####.#####.###.#.#.#.###.###########.#.###.#.#####
#.#.#.#.......#.#...#.....#...#...#.#...#...#.#.#.#...#.#...#.....#...#.#.#.....#
#.#.#.#########.#.#########.###.#.#.###.###.#.#.#.#####.#.#.#####.#####.#.#####.#
#...#.....#.....#b..#...#...#...#...#...#...#.#.#.....#...#.#y..#.......#.....#.#
###.#####.#.#######.###B#.#.#.#######.#.#.#####.#####.#.###.###.#####.#.#.#####.#
#...#...I.#f......#.....#.#.#.#...#...#.#...#...#...#.#.#.....#.....#.#...#.....#
#####.###########.#######.###.#.###.#.#####.#.###.###.###.#########.#######.#####
#o....#k........#.#.#.......#.#.#...#...#.#.#.#.....#.#...#.......#.......K.#...#
#.#####.###.#####.#.#.#####.#.#.#.#####.#.#.#.###.#.#.#.###.###.###############.#
#.#.......#...#.C.#.....#...#.#...#...#.#...#...#.#.#.#...#...#.....#...........#
#.#.#########.#.#########.###.###.#.###.#.#####.#.#.#.###.###.#####.#.#.#######.#
#...#l........#...#.....#...#...#...#...#.......#.#...#...#...#...#...#.X.#...#.#
#.###.#.#########.#V###.###.###.#####.###########.#####.###.###.#########.#.#.#.#
#...#.#.#.....#...#.#.#.#...#.#.....#...#.......#...#...#...#...........#.#.#.#.#
#####.#.#.###.#.###.#.#.#.#.#.#####.###.#.#####.###.#.#.#.###.#######.###.#.#.#W#
#.....#.#.#r#.#.#...#.#.#.#.#.#...#...#.#.#...#...#.#.#.#...#.......#...#.#.#.#.#
#.#######.#.#.#.###.#.#.#.#.#.#.#.###.#.#.###.###.#.#.#.###.###########.#.#.#.#.#
#.........#.#.#.#s..#...#.#.Q.#.#.#...#.#...#...#...#.#.............#...#.#.#...#
#.#########.#.#.#.###.###.#.###.#.#.###.###.#.#.#####.#######.#####.#.###.#.#####
#...#...#...#.#...#...#...#.#...#...#...#.#.#.#.....#...#...#.#...#...#...#...#.#
###.#Y#.###.#.#####.###.#####.#########.#.#.###.###.#####.#.###.#.#####.#####.#.#
#.....#.....#.......#...........................#.........#....q#.......#.......#
#######################################.@.#######################################
#...#.#.................#..z..............#.......#.............#...............#
#.#.#.#.#.#############.#.#.###########.#.#.#.#####.#####.#####.#.###.#########.#
#.#...#.#.#...#.#.....#.#.#.#.....#...#.#...#.#...Z.....#.#.....#.#.#.#.......#.#
#.#####.#.#.#.#.#.#.#.#.###.#.#####.#.#.#.###.#.#########.#######.#.#.#####.###.#
#.#...#.#...#.#...#.#x#.#...#.#.....#.#.#...#.....#.....#.#...#.....#.#...#.....#
#.#.#.#.#####.#####.###.#.###.#.#####.#.###.#######.###.#.#.#.#.#####.#.#.#####.#
#w..#...#...#.....#.#.....#...#.#.....#.#.#...#.....#.#...#.#...#..v#.#.#.....#.#
#.#######.#.#####.#.#.#####.###.#.#####.#.###.#.#####.#.###.#####.#.#.#.#####.###
#.#.......#.#.#...#.#.#...#.#...#.#...#.#...#.#.#.......#...#...#.#.#.#.#...#...#
#.###.#.###.#.#.###.#.#.#.#.#.###.#.#.#.#.###.#.###.#####.###.#.#.#.#.#.###.###.#
#...#.#...#...#.#.#...#.#.#...#.#.#.#...#...#.#...#.#...#.#...#.R.#.#.........#.#
###.#####.###.#.#.#.###.#.###.#.#.#.#####.#.#.###.#.#.#.#.#.#######.#.#########.#
#.#...#...#.#.#.#.....#.#...#...#.......#.#.#...#.#...#.#.#.#...#...#.#.........#
#.###.#.###.#.#.#######.###.#.#########.#.#.###.#.#######.#.#.###.###.#.#######.#
#...#...#...#.#.........#...#.#...#.....#.#...#.#.........#.#.#...#...#.#.......#
#.#######.#.#.###########.#####.#.#####.###.###.###########.#.#.#######.#########
#.........#.#.#.........#.......#.#...#.#...#...#...........#.#.#.....#.........#
#.###.#######.#.###.#####.#####.#.#.#.###.#.#.###.###########.#.#.###S#########.#
#...#.......#...#...#...#.#...#.#...#...#.#.#...#.....L.#.....#...#...#...#...#.#
#.#########.#####.###.#.###.#.###.#####.#.#####.#######.#.#########.###.#.#.#.#.#
#.#.......#.#...#.#.#.#.#...#...#...#...#...........#...#...#.#....c#...#...#.#.#
###.#####.#.#.#.#.#.###.#.#####.#####.###.###########.#####.#.#.#####.#######.#.#
#...#.......#.#...#...#...#...#...#...#.#...#.........#.....#...#.......#.......#
#.###.#######.#####.#######.#.###.#.###.###.#.###########.#.#########.#.#######.#
#.#.#.#...#...#.............#...#...#...#...#.............#.........#.#.#.....#.#
#.#.#.#.#.#.###########.#####.#.#####.###.#########################.###.#.###.#.#
#.#...#.#.#.....#.....#...#...#.#.#.....#.....#...#.......#.......#...#...#...#.#
#.#####.#.#####.#.###.#####.###.#.#.###.#####.#.###.###.###.#####.###.#####.#####
#.......#...#.#...#.#.#.....#.#.#...#...#...#.#.#.....#.........#...#.....#.....#
#.#######.#.#.#####E#.#.#####.#.#.###.#.#.#.#.#.#.#############.#.#.#####.###.#.#
#...#.....#...#...#...#.#.....#.#...#.#.#.#...#.....#..a#.....#.#.#...#.#...#.#.#
#####.#######.#.###.###.#.###.#.#.###.#.#.###########.#.#.###.###.###.#.###.###.#
#...#.#.#...#.#.#...#...#.#...#.#.#...#.#.....#.....#.#.#.#.#...#...#...#.#...#.#
#.#.#.#.#.#.#.#.#.###.#.#.#.#.#.###.###.#####.#.###.#.#.#.#.###.###.###.#.###.#.#
#.#.#.#.#.#.....#.#...#.#.#.#.#.....#.#.#.....#.#...#.#...#...#...#.#.#.#...#..i#
#.#.#.#.#.#######.#####.###.#########.#.#.#####U#.###.#######.###.#.#.#.#.#.#####
#.#n..#.......#...#...#...#.#...#.......#.......#t#...#.........#.#.#.#...#.#...#
#.#############.###.#.###.#.#.#.#.###############.#.###.#.#######.#.#.#####.#.#.#
#...............J...#.....#...#.........#...........#...#.........M.#..p......#.#
#################################################################################"""

# input = """#########
# #b.A.@.a#
# #########"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def add_point(p: Point, q: Point) -> Point:
    return Point(x=p.x + q.x, y=p.y + q.y)


up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)
directions = [up, right, down, left]

walls = set()
keys_dict: Dict[str, Point] = {}
doors_dict: Dict[Point, str] = {}
start = None
for y, line in enumerate(input.splitlines()):
    for x, c in enumerate(line):
        if c == "#":
            walls.add(Point(x, y))
        elif c.isalpha():
            if c.islower():
                keys_dict[c] = Point(x, y)
            else:
                doors_dict[Point(x, y)] = c
        elif c == "@":
            start = Point(x, y)
assert(start is not None)

# modify map for part 2
starts = [
    add_point(up, add_point(right, start)),
    add_point(up, add_point(left, start)),
    add_point(down, add_point(right, start)),
    add_point(down, add_point(left, start))
]
walls = walls | {
    start,
    add_point(up, start),
    add_point(right, start),
    add_point(down, start),
    add_point(left, start)
}


"""
work out what each door unlocks access to
can work out ht edistance between any two pairs of keys, theres not that many of them (ignore doors for this)

these two combined means that i immediately know what keys are accessable, and how far it is to get there
rather than having to do the bucket fill

this removes the whole traversal aspect of this puzzle

"""

all_keys: Set[Point] = set(keys_dict.values())


def pop_next(dict):
    min_key = min(dict)
    set_value = dict[min_key]
    return_value = set_value.pop()
    if len(set_value) == 0:
        dict.pop(min_key, None)
    return return_value, min_key

# Maps the distance to travel between two points assuming the doors are all unlocked
# If a tuple isnt in this dict, then you cannot travel between them!
distances: Dict[Tuple[Point, Point], int] = {}
for a in all_keys:
    positions_to_check = {
        0: {a}
    }
    seen_positions = set()
    while len(positions_to_check) != 0:
        pos, dist = pop_next(positions_to_check)
        if pos in seen_positions:
            continue
        seen_positions.add(pos)
        if pos in all_keys and pos != a:
            distances[(a, pos)] = dist
        for d in directions:
            new_pos = add_point(pos, d)
            if new_pos in walls:
                continue
            if dist + 1 not in positions_to_check:
                positions_to_check[dist + 1] = set()
            positions_to_check[dist + 1].add(new_pos)

# Maps a key K to the various other keys that are required to visit before being able to visit K
# And also add the distance from start to each key whilst we are at it
unlocks_required: Dict[Point, Set[Point]] = {}
for start in starts:
    positions_to_check = {
        0: {(start, frozenset())}
    }
    seen_positions = set()
    while len(positions_to_check) != 0:
        (pos, required_keys), dist = pop_next(positions_to_check)
        if pos in seen_positions:
            continue
        seen_positions.add(pos)
        new_required_keys = set()
        if pos in all_keys and pos != start:
            distances[(start, pos)] = dist
            unlocks_required[pos] = required_keys
        if pos in doors_dict:
            key_to_unlock_door = keys_dict[doors_dict[pos].lower()]
            new_required_keys.add(key_to_unlock_door)
        for d in directions:
            new_pos = add_point(pos, d)
            if new_pos in walls:
                continue
            if dist + 1 not in positions_to_check:
                positions_to_check[dist + 1] = set()
            positions_to_check[dist + 1].add((new_pos, frozenset(set(required_keys) | new_required_keys)))


def get_accessible_keys(current_pos: Point, collected_keys: Set[Point]) -> Set[Point]:
    return_points = set()
    candidate_keys = [k for k in (all_keys - collected_keys) if (current_pos, k) in distances]
    for k in candidate_keys:
        if k not in unlocks_required:
            return_points.add(k)
        elif unlocks_required[k].issubset(collected_keys):
            return_points.add(k)
    return return_points



step_mapping = {
    0: {(starts[0], starts[1], starts[2], starts[3], frozenset(set()))}
}
seen_states = set()

while True:
    (pos0, pos1, pos2, pos3, collected_keys), dist_so_far = pop_next(step_mapping)
    if len(collected_keys) == len(all_keys):
        # collected all of them
        print(dist_so_far)
        break
    if (pos0, pos1, pos2, pos3, collected_keys) in seen_states:
        # been here already, so ignore
        continue
    seen_states.add((pos0, pos1, pos2, pos3, collected_keys))

    # check robot 0 moving
    # yes i know this probably should be done in a loop, but i dont
    # want to work out how to dynamically change tuples

    accessible_keys = get_accessible_keys(pos0, collected_keys)
    for accessible_key in accessible_keys:
        new_dist = dist_so_far + distances[(pos0, accessible_key)]
        new_collected_keys = set(collected_keys)
        new_collected_keys.add(accessible_key)
        if new_dist not in step_mapping:
            step_mapping[new_dist] = set()
        step_mapping[new_dist].add((accessible_key, pos1, pos2, pos3, frozenset(new_collected_keys)))

    accessible_keys = get_accessible_keys(pos1, collected_keys)
    for accessible_key in accessible_keys:
        new_dist = dist_so_far + distances[(pos1, accessible_key)]
        new_collected_keys = set(collected_keys)
        new_collected_keys.add(accessible_key)
        if new_dist not in step_mapping:
            step_mapping[new_dist] = set()
        step_mapping[new_dist].add((pos0, accessible_key, pos2, pos3, frozenset(new_collected_keys)))

    accessible_keys = get_accessible_keys(pos2, collected_keys)
    for accessible_key in accessible_keys:
        new_dist = dist_so_far + distances[(pos2, accessible_key)]
        new_collected_keys = set(collected_keys)
        new_collected_keys.add(accessible_key)
        if new_dist not in step_mapping:
            step_mapping[new_dist] = set()
        step_mapping[new_dist].add((pos0, pos1, accessible_key, pos3, frozenset(new_collected_keys)))

    accessible_keys = get_accessible_keys(pos3, collected_keys)
    for accessible_key in accessible_keys:
        new_dist = dist_so_far + distances[(pos3, accessible_key)]
        new_collected_keys = set(collected_keys)
        new_collected_keys.add(accessible_key)
        if new_dist not in step_mapping:
            step_mapping[new_dist] = set()
        step_mapping[new_dist].add((pos0, pos1, pos2, accessible_key, frozenset(new_collected_keys)))

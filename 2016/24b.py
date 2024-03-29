from typing import Set

import file_loader

input_string = file_loader.get_input()


# input_string = """###########
# #0.1.....2#
# #.#######.#
# #4.......3#
# ###########"""



from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

def add_point(p: Point, q: Point):
    return Point(p.x + q.x, p.y + q.y)

positions = {}
walls = set()

lines = input_string.splitlines()

for y in range(len(lines)):
    for x in range(len(lines[0])):
        c = lines[y][x]
        if lines[y][x] == '#':
            walls.add(Point(x, y))
        elif lines[y][x].isnumeric():
            positions[int(lines[y][x])] = Point(x, y)
        elif lines[y][x] != '.':
            print("wtf is this", lines[y][x])



# Build adjacency matrix to find the shortest paths between any two pairs of positions

def pop_next(c):
    min_key = min(c)
    states = c[min_key]
    return_value = states.pop()
    if len(states) == 0:
        c.pop(min_key, None)
    return return_value, min_key

def shortest_distance(start: Point, end: Point, walls: Set[Point]):

    step_mapping = {
        0: {start}
    }
    visited_points = set()

    is_found = 0
    while not is_found:
        p, steps = pop_next(step_mapping)
        if p == end:
            return steps

        visited_points.add(p)

        for d in [up, down, left, right]:
            neighbour = add_point(p, d)
            if neighbour in walls:
                continue
            if neighbour in visited_points:
                continue

            if steps + 1 not in step_mapping:
                step_mapping[steps + 1] = set()
            step_mapping[steps + 1].add(neighbour)

    return is_found


from itertools import combinations


distances = {}

for i, j in combinations(positions.keys(), 2):
    distances[(i,j)] = shortest_distance(positions[i], positions[j], walls)
    distances[(j,i)] = distances[(i,j)]

# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(distances)


# not to find the shortest tour


step_mapping = {
    0: {(0,)}
}

seen_paths = set()

shortest_path = 0
while shortest_path == 0:
    path, length = pop_next(step_mapping)

    if -1 in path:
        # print(path)
        shortest_path = length
        break

    last_position = path[-1]

    added_new_position = False
    for i in positions.keys():
        if i in path:
            continue
        if (last_position, i) not in distances:
            continue
        new_length = length + distances[(last_position, i)]
        new_path = (*path, i)
        if new_length not in step_mapping:
            step_mapping[new_length] = set()
        step_mapping[new_length].add(new_path)
        added_new_position = True

    # if all positions are filled, then add in the starting point
    if not added_new_position:
        if (last_position, 0) not in distances:
            pass
        else:
            new_length = length + distances[(last_position, 0)]
            new_path = (*path, -1) # using -1 to differentiate it from 0
            if new_length not in step_mapping:
                step_mapping[new_length] = set()
            step_mapping[new_length].add(new_path)



print(shortest_path)





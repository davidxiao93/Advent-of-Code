from typing import List

import file_loader

input_string = file_loader.get_input()

threshold = 100
x_size = 0
y_size = 0

# input_string = """
# Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%"""
# threshold = 15


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Move = namedtuple("Move", ["start", "end"])

used_grid = {}
size_grid = {}

for line in input_string.splitlines()[2:]:
    words = line.split()
    _, x, y = words[0].rsplit("-", 2)
    x = int(x[1:])
    x_size = max(x_size, x)
    y = int(y[1:])
    y_size = max(y_size, y)
    size = int(words[1][:-1])
    used = int(words[2][:-1])
    p = Point(x, y)
    used_grid[p] = used
    size_grid[p] = size


def is_viable(used_grid, p: Point, q:Point):
    return q in used_grid \
           and p in used_grid \
           and used_grid[p] != 0 \
           and p != q \
           and size_grid[q] - used_grid[q] >= used_grid[p]

def get_empty_node(used_grid):
    return [k for k, v in used_grid.items() if v == 0][0]

def pretty_print(used_grid, size_grid):
    for y in range(y_size):
        for x in range(x_size):
            if x == y == 0:
                print("X ", end="")
                continue
            if x == x_size - 1 and y == 0:
                print("G ", end="")
                continue


            p = Point(x, y)
            if size_grid[p] > threshold:
                print("# ", end="")
            elif used_grid[p] == 0:
                print("e ", end="")
            else:
                print(". ", end="")
        print("")

pretty_print(used_grid, size_grid)

def add(p: Point, q: Point):
    return Point(x = p.x + q.x, y = p.y + q.y)


directions = {
    Point(x=0, y=1),
    Point(x=0, y=-1),
    Point(x=1, y=0),
    Point(x=-1, y=0)
}


def get_viable_moves(used_grid) -> List[Move]:
    moves = []
    # Make assumption that all moves will be moving data into the empty node
    empty_node = get_empty_node(used_grid)
    for d in directions:
        node_to_check = add(empty_node, d)
        if is_viable(used_grid, node_to_check, empty_node):
            moves.append(Move(start=node_to_check, end=empty_node))

    return moves

def pop_next(c):
    min_key = min(c)
    states = c[min_key]
    return_value = states.pop()
    if len(states) == 0:
        c.pop(min_key, None)
    return return_value, min_key

target_data = Point(x=x_size, y=0)

factor = x_size * y_size
def calc_score(grid, target, num_moves):
    empty_node = get_empty_node(grid)
    return factor*target.x*target.x + factor*target.y*target.y \
           + (empty_node.x-target.x)*(empty_node.x-target.x)\
            + (empty_node.y - target.y)*(empty_node.y - target.y)\
           + num_moves * num_moves * factor * factor


score_mapping = {
    calc_score(used_grid, target_data, 0): [(used_grid, target_data, 0)]
}

empty_node_visited = set()
target_node_visited = {target_data}

is_end = 0

while not is_end:
    (grid, target_data, num_moves), s = pop_next(score_mapping)
    # print("\t".join([str(num_moves), str(s), str(target_data), str(get_empty_node(grid))]))
    print(num_moves)
    if target_data == Point(x=0, y=0):
        is_end = num_moves
        break
    for move in get_viable_moves(grid):
        if (move, target_data) in empty_node_visited:
            continue
        empty_node_visited.add((move, target_data))
        new_grid = grid.copy()
        new_grid[move.end] += new_grid[move.start]
        new_grid[move.start] = 0
        new_target_data_position = target_data
        if move.start == target_data:
            new_target_data_position = move.end
            if new_target_data_position in target_node_visited:
                continue
            # Assume that the target data wil move straight across
            if new_target_data_position.y != 0:
                continue
            target_node_visited.add(new_target_data_position)
        score = calc_score(new_grid, new_target_data_position, num_moves)
        if score not in score_mapping:
            score_mapping[score] = []
        score_mapping[score].append((new_grid, new_target_data_position, num_moves + 1))


print(is_end)


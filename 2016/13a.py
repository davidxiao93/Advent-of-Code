

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

import file_loader

input_string = file_loader.get_input()
input_value = int(input_string)

start = Point(x=1, y=1)
target = Point(x=31, y=39)

# input_value = 10
# target = Point(x=7, y=4)


def is_open(p: Point) -> bool:
    if p in is_open_map:
        return is_open_map[p]
    v = p.x*p.x + 3*p.x + 2*p.x*p.y + p.y + p.y*p.y + input_value
    r = bin(v).count("1") % 2 == 0
    is_open_map[p] = r
    return r



is_open_map = {}
is_visited = set()


def pop_next(c):
    min_key = min(c)
    states = c[min_key]
    return_value = states.pop()
    if len(states) == 0:
        c.pop(min_key, None)
    return return_value, min_key


def add(p: Point, q: Point):
    return Point(x = p.x + q.x, y = p.y + q.y)

score_mapping = {
    0: {(start, 0)}
}

is_end = 0

directions = {
    Point(x=0, y=1),
    Point(x=0, y=-1),
    Point(x=1, y=0),
    Point(x=-1, y=0)
}

while not is_end:
    (current_pos, num_steps), s = pop_next(score_mapping)
    if current_pos == target:
        is_end = num_steps
    for d in directions:
        new_pos = add(current_pos, d)
        if is_open(new_pos) and new_pos not in is_visited:
            new_score = num_steps + 1
            if new_score not in score_mapping:
                score_mapping[new_score] = set()
            score_mapping[new_score].add((new_pos, num_steps + 1))
            is_visited.add(new_pos)


print(is_end)


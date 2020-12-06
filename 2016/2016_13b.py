

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

input = 1350
start = Point(x=1, y=1)
target_steps = 50

# input = 10
# target_steps = 3
# target = Point(x=7, y=4)


def is_open(p: Point) -> bool:
    if p in is_open_map:
        return is_open_map[p]
    if p.x < 0 or p.y < 0:
        r = False
    else:
        v = p.x*p.x + 3*p.x + 2*p.x*p.y + p.y + p.y*p.y + input
        r = bin(v).count("1") % 2 == 0
    is_open_map[p] = r
    return r



is_open_map = {}
visited = set()


def pop_next(c):
    min_key = min(c)
    states = c[min_key]
    return_value = states.pop()
    if len(states) == 0:
        c.pop(min_key, None)
    return return_value, min_key



def add(p: Point, q: Point):
    return Point(x = p.x + q.x, y = p.y + q.y)

step_mapping = {
    0: {start}
}


directions = {
    Point(x=0, y=1),
    Point(x=0, y=-1),
    Point(x=1, y=0),
    Point(x=-1, y=0)
}



while True:
    current_pos, num_steps = pop_next(step_mapping)
    if num_steps >= target_steps:
        break
    for d in directions:
        new_pos = add(current_pos, d)
        if is_open(new_pos) and new_pos not in visited:
            if num_steps + 1 not in step_mapping:
                step_mapping[num_steps + 1] = set()
            step_mapping[num_steps + 1].add(new_pos)
            visited.add(new_pos)


print(len(visited))


input = """vwbaicqe"""


import hashlib
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

current_pos = Point(x=0, y=0)
target_pos = Point(x=3, y=3)

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def point_add(p: Point, q:Point):
    return Point(x=p.x+q.x, y=p.y+q.y)


directions = [
    (Point(x=0, y=-1), 'U'),
    (Point(x=0, y=1), 'D'),
    (Point(x=-1, y=0), 'L'),
    (Point(x=1, y=0), 'R'),
]

def pop_next(c):
    min_key = min(c)
    states = c[min_key]
    return_value = states.pop()
    if len(states) == 0:
        c.pop(min_key, None)
    return return_value, min_key

step_mapping = {
    0: {(input, current_pos)}
}

is_found = ""
while not is_found:
    (s, p), steps = pop_next(step_mapping)

    if p == target_pos:
        is_found = s[len(input):]

    if steps + 1 not in step_mapping:
        step_mapping[steps + 1] = set()

    h = md5(s)
    for i in range(4):
        is_open = h[i] in ["b", "c", "d", "e", "f"]
        if not is_open:
            continue
        new_pos = point_add(p, directions[i][0])
        if 0 <= new_pos.x <= 3 and 0 <= new_pos.y <= 3:
            step_mapping[steps + 1].add((s + directions[i][1], new_pos))

print(is_found)


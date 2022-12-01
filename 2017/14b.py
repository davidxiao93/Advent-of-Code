from typing import List
from functools import reduce
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
def add_point(p, q):
    return Point(p.x + q.x, p.y + q.y)

import file_loader

input_string = file_loader.get_input()

# input_string = "flqrgnkx"


def shift_left(s, n):
    n = n % len(s)
    return s[n:] + s[:n]

def reverse(s, n):
    r = s[:n]
    r = r[::-1]
    return r + s[n:]

def build_lengths(input_string):
    s = []
    for c in input_string:
        s.append(ord(c))
    s.append(17)
    s.append(31)
    s.append(73)
    s.append(47)
    s.append(23)
    return s

def build_message():
    s = []
    for i in range(256):
        s.append(i)
    return s

def knot(message: List[int], lengths: List[int], current_pos = 0, skip_size = 0):
    original_pos = current_pos
    message = shift_left(message, current_pos)
    current_pos = 0
    for i in lengths:
        message = reverse(message, i)
        message = shift_left(message, i + skip_size)
        current_pos = ((current_pos - i) - skip_size) % len(message)
        skip_size += 1
    new_message = message[current_pos:] + message[:current_pos]
    return shift_left(new_message, len(message) - original_pos), (original_pos + len(message) - current_pos) % len(message), skip_size

def knot_hash_binary(input_string):
    lengths = build_lengths(input_string)
    message = build_message()

    current_pos = 0
    skip_size = 0
    for i in range(64):
        message, current_pos, skip_size = knot(message, lengths, current_pos, skip_size)

    dense = []
    for i in range(16):
        x = reduce(lambda a, b: a ^ b, message[i * 16: i * 16 + 16])
        dense.append(x)

    return "".join([format(d, 'b').zfill(8) for d in dense])




used = set()
for y in range(128):
    for x, c in enumerate(knot_hash_binary(input_string + "-" + str(y))):
        if c == "1":
            used.add(Point(x, y))


up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)
directions = [up, down, left, right]

counter = 0
while len(used) != 0:
    counter += 1
    to_check = { used.pop() }
    next_group = set()
    while len(to_check) != 0:
        next_point = to_check.pop()

        for d in directions:
            candidate = add_point(next_point, d)
            if 0 <= candidate.x < 128 \
                    and 0 <= candidate.y < 128 \
                    and candidate in used\
                    and candidate not in next_group:
                to_check.add(candidate)
        next_group.add(next_point)
    used -= next_group

print(counter)
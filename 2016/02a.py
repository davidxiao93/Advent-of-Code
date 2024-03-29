import file_loader

input_string = file_loader.get_input()

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

current_pos = Point(x=1, y=1)

def move_left(current_pos):
    x = current_pos.x - 1
    if x < 0:
        x = 0
    return Point(x, current_pos.y)

def move_right(current_pos):
    x = current_pos.x + 1
    if x > 2:
        x = 2
    return Point(x, current_pos.y)

def move_down(current_pos):
    y = current_pos.y - 1
    if y < 0:
        y = 0
    return Point(current_pos.x, y)

def move_up(current_pos):
    y = current_pos.y + 1
    if y > 2:
        y = 2
    return Point(current_pos.x, y)

def get_key():
    return (2 - current_pos.y) * 3 + current_pos.x + 1

answer = ""
for line in input_string.splitlines():
    for c in line:
        if c == "L":
            current_pos = move_left(current_pos)
        if c == "R":
            current_pos = move_right(current_pos)
        if c == "U":
            current_pos = move_up(current_pos)
        if c == "D":
            current_pos = move_down(current_pos)
    answer += str(get_key())

print(answer)



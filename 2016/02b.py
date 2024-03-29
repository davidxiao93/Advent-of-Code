import file_loader

input_string = file_loader.get_input()

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

current_pos = Point(x=-2, y=0) # Starting at 5. Origin is 7

def move_left(current_pos):
    x = current_pos.x - 1
    if abs(x) + abs(current_pos.y) > 2:
        x = current_pos.x
    return Point(x, current_pos.y)

def move_right(current_pos):
    x = current_pos.x + 1
    if abs(x) + abs(current_pos.y) > 2:
        x = current_pos.x
    return Point(x, current_pos.y)

def move_down(current_pos):
    y = current_pos.y - 1
    if abs(current_pos.x) + abs(y) > 2:
        y= current_pos.y
    return Point(current_pos.x, y)

def move_up(current_pos):
    y = current_pos.y + 1
    if abs(current_pos.x) + abs(y) > 2:
        y = current_pos.y
    return Point(current_pos.x, y)

pos_to_key = {
    Point(0,2): "1",
    Point(-1,1): "2",
    Point(0,1): "3",
    Point(1,1): "4",
    Point(-2,0): "5",
    Point(-1,0): "6",
    Point(0,0): "7",
    Point(1,0): "8",
    Point(2,0): "9",
    Point(-1,-1): "A",
    Point(0,-1): "B",
    Point(1,-1): "C",
    Point(0,-2): "D"
}

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
    answer += pos_to_key[current_pos]

print(answer)


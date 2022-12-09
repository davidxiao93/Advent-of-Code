from collections import namedtuple

import file_loader

input_string = file_loader.get_input()

Point = namedtuple("Point", ["x", "y"])

knots = [
    Point(0,0)
    for i in range(10)
]

tail_visited = set()
tail_visited.add(knots[-1])

def clamp(num):
    num = max(min(num, 1), -1)
    return num

def move_follower(head, tail):
    dx = 0
    dy = 0
    if head.x - tail.x >= 2:
        dx = 1
        dy = clamp(head.y - tail.y)
    elif head.x - tail.x <= -2:
        dx = -1
        dy = clamp(head.y - tail.y)
    elif head.y - tail.y >= 2:
        dx = clamp(head.x - tail.x)
        dy = 1
    elif head.y - tail.y <= -2:
        dx = clamp(head.x - tail.x)
        dy = -1
    return Point(tail.x + dx, tail.y + dy)

def move_head(head, dir):
    if dir == "U":
        return Point(head.x, head.y + 1)
    elif dir == "D":
        return Point(head.x, head.y - 1)
    elif dir == "L":
        return Point(head.x - 1, head.y)
    elif dir == "R":
        return Point(head.x + 1, head.y)

for line in input_string.splitlines():
    dir = line.split()[0]
    count = int(line.split()[1])
    for i in range(count):
        knots[0] = move_head(knots[0], dir)
        for i in range(len(knots) - 1):
            knots[i+1] = move_follower(knots[i], knots[i+1])
        tail_visited.add(knots[-1])

print(len(tail_visited))
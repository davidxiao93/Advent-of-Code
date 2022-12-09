import file_loader
from collections import namedtuple

input_string = file_loader.get_input()

Point = namedtuple("Point", ["x", "y"])

head = Point(0,0)
tail = Point(0,0)

tail_visited = set()
tail_visited.add(tail)

def move_tail():
    dx = 0
    dy = 0
    if head.x - tail.x >= 2:
        dx = 1
        dy = head.y - tail.y
    elif head.x - tail.x <= -2:
        dx = -1
        dy = head.y - tail.y
    elif head.y - tail.y >= 2:
        dx = head.x - tail.x
        dy = 1
    elif head.y - tail.y <= -2:
        dx = head.x - tail.x
        dy = -1
    return Point(tail.x + dx, tail.y + dy)

for line in input_string.splitlines():
    dir = line.split()[0]
    count = int(line.split()[1])
    for i in range(count):
        if dir == "U":
            head = Point(head.x, head.y + 1)
        elif dir == "D":
            head = Point(head.x, head.y - 1)
        elif dir == "L":
            head = Point(head.x - 1, head.y)
        elif dir == "R":
            head = Point(head.x + 1, head.y)
        tail = move_tail()
        tail_visited.add(tail)

print(len(tail_visited))
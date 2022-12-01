import file_loader

input_string = file_loader.get_input()

# input_string = """     |
#      |  +--+
#      A  |  C
#  F---|----E|--+
#      |  |  |  D
#      +B-+  +--+
# """

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])

def add_point(p: Point, q: Point):
    return Point(p.x+q.x, p.y+q.y)

up = Point(x=0, y=-1)
down = Point(x=0, y=1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

reversed_direction = {
    up: down,
    down: up,
    left: right,
    right: left
}

points = {}
current_point = None
current_direction = down

for y, line in enumerate(input_string.splitlines()):
    for x, c in enumerate(line):
        if c != " ":
            if y == 0:
                current_point = Point(x, y)
            points[Point(x, y)] = c

if current_point is None:
    print("Failed to find starting point")
    exit(1)


visited = ""
steps = 0
while True:
    steps += 1
    next_point = add_point(current_point, current_direction)
    if next_point not in points:
        break
    c = points[next_point]
    if c.isalpha():
        visited += c
    if c == "+":
        # find new direction
        for d in {up, down, left, right} - {reversed_direction[current_direction]}:
            if add_point(next_point, d) in points:
                current_direction = d
                break


    current_point = next_point


print(steps)






import file_loader

input_string = file_loader.get_input()



from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x=0, y=1)
down = Point(x=0, y=-1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)

directions = [right, down, left, up]
current_direction = 0


current_pos = Point(x=0, y=0)

def add_point(p, q):
    return Point(x=p.x+q.x, y=p.y+q.y)

def mul_point(p, v):
    return Point(x=v*p.x, y=v*p.y)

for line in input_string.splitlines():
    action = line[0]
    value = int(line[1:])
    if action == "N":
        current_pos = add_point(current_pos, mul_point(up, value))
    elif action == "S":
        current_pos = add_point(current_pos, mul_point(down, value))
    elif action == "E":
        current_pos = add_point(current_pos, mul_point(right, value))
    elif action == "W":
        current_pos = add_point(current_pos, mul_point(left, value))
    elif action == "L":
        current_direction = (current_direction - int(value/90)) % 4
    elif action == "R":
        current_direction = (current_direction + int(value/90)) % 4
    elif action == "F":
        current_pos = add_point(current_pos, mul_point(directions[current_direction], value))
    else:
        print("wtf")
        exit(1)


print(abs(current_pos.x) + abs(current_pos.y))
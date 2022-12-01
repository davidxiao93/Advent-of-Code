import file_loader

input_string = file_loader.get_input()



from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

up = Point(x=0, y=1)
down = Point(x=0, y=-1)
left = Point(x=-1, y=0)
right = Point(x=1, y=0)



waypoint = Point(x=10, y=1)
current_pos = Point(x=0, y=0)

def add_point(p, q):
    return Point(x=p.x+q.x, y=p.y+q.y)

def mul_point(p, v):
    return Point(x=v*p.x, y=v*p.y)

def rot_ccw_point(p, v):
    v = v % 4
    for i in range(v):
        p = Point(x=-1*p.y, y=p.x)
    return p


for line in input_string.splitlines():
    action = line[0]
    value = int(line[1:])
    if action == "N":
        waypoint = add_point(waypoint, mul_point(up, value))
    elif action == "S":
        waypoint = add_point(waypoint, mul_point(down, value))
    elif action == "E":
        waypoint = add_point(waypoint, mul_point(right, value))
    elif action == "W":
        waypoint = add_point(waypoint, mul_point(left, value))
    elif action == "L":
        waypoint = rot_ccw_point(waypoint, int(value/90))
    elif action == "R":
        waypoint = rot_ccw_point(waypoint, -1*int(value/90))
    elif action == "F":
        current_pos = add_point(current_pos, mul_point(waypoint, value))
    else:
        print("wtf")
        exit(1)


print(abs(current_pos.x) + abs(current_pos.y))
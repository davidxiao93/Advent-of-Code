import file_loader

input_string = file_loader.get_input()


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

directions = [
    Point(x=0, y=1), # North
    Point(x=1, y=0), # East
    Point(x=0, y=-1), # South
    Point(x=-1, y=0) # West
]

current_direction = 0

def turn_left(cd):
    cd -= 1
    if cd < 0:
        cd += 4
    return cd

def turn_right(cd):
    cd += 1
    if cd >= 4:
        cd -= 4
    return cd

current_pos = Point(x=0, y=0)

def move(cp: Point, d: int):
    return Point(x=cp.x + d*directions[current_direction].x,
                 y=cp.y + d*directions[current_direction].y)


input_string = input_string.replace(",", "")

for i in input_string.split():
    if i[0] == "L":
        current_direction = turn_left(current_direction)
    elif i[0] == "R":
        current_direction = turn_right(current_direction)
    else:
        print("Error, cannot understand instruction")
        exit(1)

    d = int(i[1:])
    current_pos = move(current_pos, d)

print(abs(current_pos.x) + abs(current_pos.y))

